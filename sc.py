import subprocess
import os

def connect_and_get_sysid():
    try:
        sqlplus_command = "sqlplus /nolog"
        sqlplus_process = subprocess.Popen(sqlplus_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
        sqlplus_process.stdin.write(b"connect / as sysdba\n")
        output, error = sqlplus_process.communicate()
        output_str = output.decode("utf-8").strip()
        if "ORA-" in output_str:
            print("Error connecting to Oracle:", output_str)
            return 1
    except Exception as e:
        print("Error connecting to Oracle:", str(e))
        return 1

    try:
        sqlplus_process.stdin.write(b"set head off\n")
        sqlplus_process.stdin.write(b"select distinct id from abc.databases order by 1;\n")
        sqlplus_process.stdin.write(b"exit\n")
        output, error = sqlplus_process.communicate()
        output_str = output.decode("utf-8").strip()
        if "ORA-" in output_str:
            print("Error executing query:", output_str)
            return 1
        else:
            sysid_list = output_str.split("\n")
            print("List of IDs:", sysid_list)
            return 0
    except Exception as e:
        print("Error executing query:", str(e))
        return 1

# Example usage
exit_code = connect_and_get_sysid()
print("Exit code:", exit_code)

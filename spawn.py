import subprocess

# alt + mouse drag

p = subprocess.Popen("xinput test-xi2 --root", stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True, bufsize=1)

event = []
cc = ""

m1 = m2 = None 
size = None

while not p.poll():
    out = p.stdout.readline().decode().strip()
    #print(out)

    ev = {
            "device" : '',
            "detail" : '',
            "root" : '',
        }

    if out.startswith("EVENT"):
        ccparse = cc.replace(":","")
        cs = ccparse.split()
        try:
            ev = {
                    "device" : cs[cs.index("device")+1],
                    "detail" : cs[cs.index("detail")+1],
                    "root" : cs[cs.index("root")+1],
                }
        except Exception as e:
            pass

        # print(ccparse)
        if "motion" not in ccparse.lower() or "raw" not in ccparse.lower():
            if "press" in ccparse.lower() or "release" in ccparse.lower():
                if ev['device'] == '10' or ev['device'] == '15':
                    event.append(ev)
                    # print(ccparse)
                    # print(ev)
                    # print("-"*10)

                    lev = event[-1]
                    if lev['device'] == '10':
                        if m1 == None:
                            m1 = tuple(map(float, lev['root'].split('/')))
                        else:
                            m2 = tuple(map(float, lev['root'].split('/')))
                            print(m1)
                            print(m2)
                            size = (abs(m2[0]-m1[0]), abs(m2[1]-m1[1]))
                            print(size)
                            if min(size) > 100:
                                os.
                            m1 = None

        cc = out 
    else:
        cc += "\n"+out


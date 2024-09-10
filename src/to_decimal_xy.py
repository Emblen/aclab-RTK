import calc_xy
import click
import os

pwd = os.getcwd()
@click.command()
@click.option('--ubx_txt', '-txt', default="", required=True)
@click.option('--output_dir', '-outdir', default=f"{pwd}", required=True)

def main(ubx_txt, output_dir):
    s = ubx_txt
    name = s.split("\\")[-1].split(".")[0]

    f = open(f"{output_dir}/{name}.txt","r")
    # f1 = open(f"{output_dir}/{name}_d.txt", "w")
    f2 = open(f"{output_dir}/{name}_xy.txt", "w")
    while True:
        try:
            data = str(f.readline()) # GPSデーターを読み、文字列に変換
            index =  data.find('$GNGGA')
            if data == "":
                break
            if index != -1:
                global now_msg
                now_msg = data[index:len(data)-1]
                now_msg_array = now_msg.split(',')

                latitude_d = round(float(now_msg_array[2])//100 + float(now_msg_array[2])%100/60, 8)
                longtitude_d = round(float(now_msg_array[4])//100 + float(now_msg_array[4])%100/60, 8)
                latitude_d = "{:.8f}".format(latitude_d)
                longtitude_d = "{:.8f}".format(longtitude_d)

                # f1.write(now_msg_array[1]+","+str(latitude_d)+","+str(longtitude_d)+"\n")
                
                # calc xy pos
                x, y = calc_xy.calc_xy(float(latitude_d), float(longtitude_d))
                f2.write(f"{now_msg_array[1]}, {x}, {y}\n")
                
        except KeyboardInterrupt:
            break
    f.close()
    # f1.close()
    f2.close()
    
    print(f"Successfully output result to {output_dir} directory")

if __name__ == "__main__":
    main()
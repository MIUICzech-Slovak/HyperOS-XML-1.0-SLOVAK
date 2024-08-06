  find -type f \( -path '*/res/values-sk*/*.xml' -o -path '*/res/values-sk*-mcc9998-mnc9999/*.xml' \) \( -name 'arrays.xml' -o -name 'plurals.xml' -o -name 'strings.xml' \) | cpio -pd $xml_out_dir


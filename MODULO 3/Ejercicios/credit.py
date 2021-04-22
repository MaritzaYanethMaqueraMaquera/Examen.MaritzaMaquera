  $number=preg_replace('/\D/', '', $number);


  $number_length=strlen($number);
  $parity=$number_length % 2;


  $total=0;
  for ($i=0; $i<$number_length; $i++) {
    $digit=$number[$i];

    if ($i % 2 == $parity) {
      $digit*=2;

      if ($digit > 9) {
        $digit-=9;
      }
    }

    $total+=$digit;
  }


  return ($total % 10 == 0) ? TRUE : FALSE;

}
?>



#_______________________________________________
function check_cc($cc, $extra_check = false){
    $cards = array(
        "visa" => "(4\d{12}(?:\d{3})?)",
        "amex" => "(3[47]\d{13})",
        "jcb" => "(35[2-8][89]\d\d\d{10})",
        "maestro" => "((?:5020|5038|6304|6579|6761)\d{12}(?:\d\d)?)",
        "solo" => "((?:6334|6767)\d{12}(?:\d\d)?\d?)",
        "mastercard" => "(5[1-5]\d{14})",
        "switch" => "(?:(?:(?:4903|4905|4911|4936|6333|6759)\d{12})|(?:(?:564182|633110)\d{10})(\d\d)?\d?)",
    );
    $names = array("Visa", "American Express", "JCB", "Maestro", "Solo", "Mastercard", "Switch");
    $matches = array();
    $pattern = "#^(?:".implode("|", $cards).")$#";
    $result = preg_match($pattern, str_replace(" ", "", $cc), $matches);
    if($extra_check && $result > 0){
        $result = (validatecard($cc))?1:0;
    }
    return ($result>0)?$names[sizeof($matches)-2]:false;
}

# EJEMPLO DE ENTRADA
$cards = array(
    "378282246310005",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

# Prueba 1
$cards = array(
    "378282246310005",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

378282246310005 - AMEX

# Prueba 2
$cards = array(
    "371449635398431",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

371449635398431 - AMEX

# Prueba 3
$cards = array(
    "5555555555554444",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

5555555555554444 - MASTERCARD

# Prueba 4
$cards = array(
    "5105105105105100",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

5105105105105100 - MASTERCARD

# Prueba 5
$cards = array(
    "4111 1111 1111 1111",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

4111 1111 1111 1111 - VISA

# Prueba 5
$cards = array(
    "4012888888881881",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

4012 8888 8888 1881 - VISA

# Prueba 6
$cards = array(
    "1234567890",
);

foreach($cards as $c){
    $check = check_cc($c, true);
    if($check!==false)
        echo $c." - ".$check;
    else
        echo "$c - INVALID";
    echo "<br/>";
}

1234567890 - INVALID
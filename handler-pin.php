<?php
// Retrieve the PIN from the input data
$pin = $_POST['pin'];

// Play audio to confirm the entered PIN
$response = '<?xml version="1.0" encoding="UTF-8"?>
<Response>
  <Say>You entered '.$pin.'. Thank you. Please hold while we verify your PIN.</Say>
  <Pause length="10"/>
  <Say>Verification successful. You will now be connected to the next available agent.</Say>
  <Dial>+1234567890</Dial>
</Response>';

// Return the VoiceXML response
header('Content-type: text/xml');
echo $response;
?>

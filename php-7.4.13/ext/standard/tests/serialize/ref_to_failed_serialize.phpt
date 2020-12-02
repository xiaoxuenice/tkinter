--TEST--
References to objects for which Serializable::serialize() returned NULL should use N;
--FILE--
<?php

class NotSerializable implements Serializable {
    public function serialize() {
        return null;
    }

    public function unserialize($serialized) {
    }
}

$obj = new NotSerializable();
$data = [$obj, $obj];
var_dump($s = serialize($data));
var_dump(unserialize($s));

?>
--EXPECT--
string(18) "a:2:{i:0;N;i:1;N;}"
array(2) {
  [0]=>
  NULL
  [1]=>
  NULL
}

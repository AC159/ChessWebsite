//Global variables:
var numberClicks = 0;//Number of times clicked in order to move a piece.
var selectedPiece;
var piece_id;

function selectedSquare(clicked_id) {

  if(document.getElementById(clicked_id).innerHTML === "" && numberClicks === 0){
    numberClicks = 0;
    return;//Making an empty cell not selectable.
  }
  else {
    numberClicks++;
  }
  if (numberClicks === 2) {
    movePiece(clicked_id);
  }


//White pieces
  if (document.getElementById(clicked_id).innerHTML === "♖") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♘") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♗") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♔") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♕") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♙") {
    selectPiece(clicked_id);
  }
  //End of white pieces. Start of black pieces:
  if (document.getElementById(clicked_id).innerHTML === "♜") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♞") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♝") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♛") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♚") {
    selectPiece(clicked_id);
  }
  if (document.getElementById(clicked_id).innerHTML === "♟") {
    selectPiece(clicked_id);
  }

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------
  function selectPiece() {

    if (numberClicks === 1) {
      document.getElementById(clicked_id).style.backgroundColor = "yellow";//Setting the background color of the selected square.
      selectedPiece = document.getElementById(clicked_id).innerHTML;//Selecting the piece.
      piece_id = clicked_id;//Saving the id of the first selected piece.
    }
  }
}

//-----------------------------------------------------------------------------------------------------------------------------------------------------------------
function movePiece(id){

  if (numberClicks === 2 && piece_id !== id) {
    if (document.getElementById(piece_id).innerHTML === "♟" || document.getElementById(piece_id).innerHTML === "♙"){
      is_legal_move(id);//Checking if it is a legal pawn move.
    }
     //Moving the piece to new location if it is not the same location.
    document.getElementById(id).style.backgroundColor = "yellow";//Setting the background color of the selected square.
    document.getElementById(id).innerHTML = selectedPiece;
    numberClicks = 0;
    if(document.getElementById(piece_id).innerHTML === "♙" ||
       document.getElementById(piece_id).innerHTML === "♕" ||
       document.getElementById(piece_id).innerHTML === "♔" ||
       document.getElementById(piece_id).innerHTML === "♘" ||
       document.getElementById(piece_id).innerHTML === "♖" ||
        document.getElementById(piece_id).innerHTML === "♗"
    ){
    document.getElementById("board-caption").innerHTML = "Black's turn";
  }
  else if(document.getElementById(piece_id).innerHTML === "♟" ||
       document.getElementById(piece_id).innerHTML === "♚" ||
       document.getElementById(piece_id).innerHTML === "♛" ||
       document.getElementById(piece_id).innerHTML === "♝" ||
       document.getElementById(piece_id).innerHTML === "♜" ||
        document.getElementById(piece_id).innerHTML === "♞"
    ){
    document.getElementById("board-caption").innerHTML = "White's turn";
  }
  document.getElementById(piece_id).innerHTML = "";//Empty the first square from which the selected piece moved.
  }
  else if (piece_id === id){
    numberClicks = 0;
    document.getElementById(id).style.backgroundColor = "yellow";//Setting the background color of the selected square.
  }

  reset_Border_Colors();

}
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------
function reset_Border_Colors(){
  let white_chessboard = document.getElementsByClassName("white");
  for(let i = 0; i < white_chessboard.length; i++) {
    //Resetting the background color for white squares:
    white_chessboard[i].style.backgroundColor = "wheat";//Setting the background color of the selected square.
  }
  let black_chessboard = document.getElementsByClassName("black");
  for(let i = 0; i < black_chessboard.length; i++){
    black_chessboard[i].style.backgroundColor = "burlywood";//Setting the background color of the selected square.
  }

}
//---------------------------------------------------------------------------------------------------------------------------------------------------------------------
function is_legal_move(destination_id){

}





//---------------------------------------------------------------------------------------------------------------------------------------------------------------------
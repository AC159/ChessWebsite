
var chessGame = {};
var options = {
  animated: false,
  imagesPath: "../static/images/wikipedia/"
};

chessGame = new AbChess('board', options); //Creating the board
chessGame.setFEN();


function new_Game(){
   return chessGame.reset;
}

function flip_board(){
  return chessGame.flip();
}
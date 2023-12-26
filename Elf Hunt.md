When intercept the game portal, we observe following interesting things:
1. FWT token `eyJhbGciOiJub25lIiwidHlwIjoiSldUIn0.eyJzcGVlZCI6LTUwMH0` decode: `{"alg":"none","typ":"JWT"}` and `{"speed":-500}`. Looks like we can modify game speed base on this token
2. in the returned HTML we see some embedded js function such as `function create()` and `function update()`


Beside modifying the game speed, we now can modify 

1. ELF's spawn location:
   ```
    function create() {
   // ... other code ...
   const a = Phaser.Math.Between(100, 700),
   s = elves.create(a, 2 * this.cameras.main.centerY, "elf")
   // ... other code ...
   ```
   Change  X Y in create method such as: `s = elves.create(this.cameras.main.centerX + 100, this.cameras.main.centerY, "elf")`
2. Stop Elf when crosshair is near them
   ```
   function update(){
   // ... other code...
   if (Phaser.Math.Distance.Between(crosshair.x, crosshair.y, e.x, e.y) < 75 && !e.isHit) {
      e.setVelocityX(0);
      e.setVelocityY(0);
   // or kill them without clicking
   }
    // ... other code...
   ```
3. Modify the Spawm Speed: 
   Modify the delay time in following code such as `Phaser.Math.Between(4, 5)`
   ```
   function create(){
   // ... other code ...
   this.time.addEvent({ delay: Phaser.Math.Between(200, 1e3), callback: spawnElf, callbackScope: this })
   // ... other code ...
   ```
   
5. We and patch JWT with "w" key to true like `{"speed":-500,"w":true}`

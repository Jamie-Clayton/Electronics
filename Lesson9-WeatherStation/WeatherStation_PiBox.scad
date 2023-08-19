//  Set the render quality
$fn = 360;
                                                                                           
Pi4Board();

// Raspberry PI 4 Board
module Pi4Board(){

    BoardLength = 85;
    BoardWidth = 56;
    BoardThinkness = 1.6;
    MountingHoleDiameter = 2.7;
    mountingHoleEdgeOffset = 3.5;
    mountingStandOffHeight = BoardThinkness *3;

difference(){
    
        //  Create the base of the Pi's 
        color("green")
            linear_extrude(height = BoardThinkness)
            square([BoardWidth, BoardLength]);
        
        // Create the Mounting holes
        color("yellow") 
            // Closest to xyz
            translate([mountingHoleEdgeOffset,  mountingHoleEdgeOffset, 0])
            cylinder(h=mountingStandOffHeight ,d=MountingHoleDiameter, center=true);
            
            // Clockwise through xy
            translate([mountingHoleEdgeOffset,  BoardLength - mountingHoleEdgeOffset, 0])
            cylinder(h=mountingStandOffHeight ,d=MountingHoleDiameter, center=true);
    
            translate([BoardWidth - mountingHoleEdgeOffset,  BoardLength -mountingHoleEdgeOffset, 0])
            cylinder(h=mountingStandOffHeight ,d=MountingHoleDiameter, center=true);
    
            translate([BoardWidth - mountingHoleEdgeOffset,  mountingHoleEdgeOffset, 0])
            cylinder(h=mountingStandOffHeight ,d=MountingHoleDiameter, center=true);
            
            
    }    
}


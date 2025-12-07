# Builder Pattern :  The Builder Pattern is a creational design pattern that lets you construct complex objects step-by-step.
# It allows you to produce different types and representations of an object using the same construction code.

# Here is a clean implementation of the Builder Pattern used to build a Computer system.
#Step1: This is the object we want to build. It has many parts, making it hard to initialize in a single line.

class Computer:
    def __init__(self):
        self.cpu = None
        self.ram = None
        self.storage = None
        self.gpu = None

    def __str__(self):
        return f"Computer [CPU={self.cpu}, RAM={self.ram}, Storage={self.storage}, GPU={self.gpu}]"

# Step.2. The Builder (The Interface)
# This defines the methods for creating the different parts of the product.
# Notice that each method returns self. This allows for Method Chaining (e.g., .set_cpu().set_ram()).


class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self  # Return self to allow chaining

    def set_ram(self, ram):
        self.computer.ram = ram
        return self

    def set_storage(self, storage):
        self.computer.storage = storage
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def build(self):
        return self.computer


# step 3. The Director (Optional)
# The Director is responsible for executing the building steps in a specific sequence. 
# It is helpful if you have pre-defined configurations (like a standard "Gaming PC" vs. an "Office PC").

class ComputerDirector:
    def __init__(self, builder):
        self.builder = builder

    def build_gaming_pc(self):
        return (self.builder
                .set_cpu("Intel Core i9")
                .set_ram("32GB")
                .set_storage("1TB SSD")
                .set_gpu("NVIDIA RTX 4090")
                .build())

    def build_office_pc(self):
        return (self.builder
                .set_cpu("Intel Core i5")
                .set_ram("16GB")
                .set_storage("512GB SSD")
                .set_gpu("Integrated Graphics")
                .build())


# 4. Client Code
# Here is how you use the pattern in practice.

def main():
    # Example 1: Custom Build (Method Chaining)
    builder = ComputerBuilder()
    my_custom_pc = (builder
                    .set_cpu("AMD Ryzen 7")
                    .set_ram("64GB")
                    .set_storage("2TB NVMe")
                    # Note: We skipped GPU, leaving it None (optional)
                    .build())
    
    print("Custom PC:")
    print(my_custom_pc)

    print("-" * 20)

    # Example 2: Using a Director for standard builds
    director = ComputerDirector(ComputerBuilder())
    gaming_pc = director.build_gaming_pc()
    
    print("Gaming PC:")
    print(gaming_pc)

if __name__ == "__main__":
    main()
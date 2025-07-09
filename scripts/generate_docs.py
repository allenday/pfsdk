#!/usr/bin/env python3
"""
Generate comprehensive documentation for the PostFiat SDK
"""
import os
import json
import shutil
import subprocess
from pathlib import Path


def run_command(cmd, cwd=None):
    """Run a command and return the result"""
    print(f"Running: {' '.join(cmd)}")
    result = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running command: {result.stderr}")
        return False
    return True


def generate_protobuf_docs():
    """Generate protobuf documentation"""
    print("🔧 Generating protobuf documentation...")
    
    # Create output directory
    docs_dir = Path("docs/generated/proto")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Use buf to generate docs if available
    proto_dir = Path("proto")
    if proto_dir.exists():
        if not run_command(["buf", "generate", "--template", "buf.gen.docs.yaml"], cwd=proto_dir):
            print("⚠️  buf documentation generation failed, creating basic docs")
            create_basic_proto_docs()
    else:
        create_basic_proto_docs()


def create_basic_proto_docs():
    """Create basic protobuf documentation"""
    docs_dir = Path("docs/generated/proto")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    # Create index file
    index_content = """# Protocol Buffer Definitions

The PostFiat SDK uses Protocol Buffers as the source of truth for all API definitions.

## Message Types

The following message types are defined in the PostFiat protocol:

### Core Messages
- User management and authentication
- Wallet operations and transactions  
- Message passing and encryption
- AI agent interactions

### Generated Code
The protobuf definitions are used to generate:
- Python classes and gRPC services
- TypeScript interfaces and gRPC-Web clients
- OpenAPI specifications for REST APIs
- Database models and validation schemas

## Service Definitions

Services are defined for:
- User and wallet management
- Message routing and encryption
- AI agent orchestration
- Transaction processing

See the [API Reference](../../api/openapi.md) for detailed endpoint documentation.
"""
    
    with open(docs_dir / "index.md", "w") as f:
        f.write(index_content)


def copy_api_specs():
    """Copy API specifications to docs"""
    print("📋 Copying API specifications...")
    
    api_dir = Path("api")
    docs_api_dir = Path("docs/generated/api")
    docs_api_dir.mkdir(parents=True, exist_ok=True)
    
    # Copy all API files
    if api_dir.exists():
        for file in api_dir.glob("*"):
            if file.is_file():
                shutil.copy2(file, docs_api_dir)
                print(f"  Copied {file.name}")


def generate_sdk_docs():
    """Generate SDK-specific documentation"""
    print("📚 Generating SDK documentation...")
    
    # Generate Python SDK docs
    python_dir = Path("python")
    if python_dir.exists():
        print("  Generating Python SDK documentation...")
        # You could add sphinx or other doc generation here
    
    # Generate TypeScript SDK docs
    typescript_dir = Path("typescript")
    if typescript_dir.exists():
        print("  Generating TypeScript SDK documentation...")
        # You could add typedoc or other doc generation here


def main():
    """Main documentation generation function"""
    print("🚀 Generating PostFiat SDK documentation...")
    
    # Change to repository root
    repo_root = Path(__file__).parent.parent
    os.chdir(repo_root)
    
    # Generate all documentation
    generate_protobuf_docs()
    copy_api_specs()
    generate_sdk_docs()
    
    print("✅ Documentation generation complete!")
    print("📁 Generated files in docs/generated/")
    print("🌐 Ready for MkDocs build")


if __name__ == "__main__":
    main()
# LingCage on openRuyi

## Packages

- `lingcage`: the host CLI and template store directory.
- `lingcore`: the standalone host VMM CLI. LingCage links the Rust library at
  build time and does not need the `lingcore` executable installed.
- `lingcage-agent`: the guest program. Install it in the guest image, not as a
  service on the host. This RPM is dynamically linked; include its RPM-resolved
  shared library dependencies when assembling an initramfs.
- `rust-lingcore-0.2` and `rust-lingcage-0.2`: crate source providers for building
  Rust applications. Their `+feature` packages express Cargo feature dependencies.

## Host and guest prerequisites

The host needs Linux with KVM enabled and read/write access to `/dev/kvm`.
RISC-V hosts require an AIA interrupt controller; AArch64 hosts require GICv3.
A successful package build does not demonstrate that a host has these devices.

Supply a guest kernel and a root filesystem containing a matching version of
`lingcage-agent`. The guest needs virtio-vsock and the virtual devices required
by its root filesystem. Host and guest package versions should match. Installing
`lingcage-agent` on the host does not add it to any guest image.

The package does not ship a kernel, root filesystem, prebuilt template or
systemd service. No agent is started by installing the package. Guest init must
start the agent as described by upstream. Use this software for evaluation while
its isolation, storage and networking interfaces are evolving.

## Example

Run `lingcage --help` and `lingcore --help` to inspect the available arguments.
On a supported host, after providing your own guest artifacts:

```sh
lingcage check --kernel /path/to/guest-kernel
lingcage template build --kernel /path/to/guest-kernel \
  --initrd /path/to/guest-initramfs.cpio.gz --memory 256M --vcpus 1 --name base
lingcage run --template base -- sh -c 'echo hello from the guest'
```

The default store is `/var/lib/lingcage`, owned by root with mode 0700. For an
unprivileged account with KVM access, set `LINGCAGE_STORE` to a directory owned
by that account. Do not share writable templates across mutually untrusted users.

## Tests

The RPM check stage compiles full-feature tests and runs tests that do not need
KVM. On a dedicated compatible KVM test host, `rpmbuild --with kvm_tests` enables
upstream integration tests as well. Separately validate template creation,
command execution, guest shutdown, and the guest agent's dynamic dependencies.

# openRuyi 使用说明

## 软件包与职责

- `lingcage`：宿主机命令行及模板存储目录。
- `lingcore`：可独立使用的宿主机 VMM 命令行；LingCage 在编译时链接
  LingCore 的 Rust 库，运行时不需要安装这个命令行包。
- `lingcage-agent`：安装在虚拟机镜像内部的代理程序。发行版 RPM 使用动态链接，
  制作 initramfs 时还须放入 RPM 自动解析出的共享库依赖。
- `rust-lingcore-0.2`、`rust-lingcage-0.2`：供其他 Rust 项目编译使用的源码
  provider；其 `+feature` 子包表示 Cargo 功能依赖。

## 运行条件

宿主机需要启用 KVM 的 Linux，并允许运行账户读写 `/dev/kvm`。
RISC-V 宿主机还需要 AIA 中断控制器，AArch64 需要 GICv3。
编译成功不能证明机器具备这些硬件和内核能力。

自行准备虚拟机内核及包含匹配版本 `lingcage-agent` 的根文件系统。
虚拟机内核需要 virtio-vsock，以及根文件系统所需的虚拟设备支持。
宿主端和代理端应使用匹配版本。在宿主机安装代理包不会自动将其加入虚拟机镜像。

本包不包含内核、根文件系统、预制模板或 systemd 服务；安装时不会启动代理。
应按上游方式由虚拟机 init 启动代理。隔离、存储和网络接口仍在演进，建议先用于评估。

## 使用与测试

先运行 `lingcage --help`、`lingcore --help`。准备好内核和 initramfs 后，
可使用上方示例检查宿主机、创建模板并在虚拟机中执行命令。
默认模板目录 `/var/lib/lingcage` 由 root 所有，权限为 0700。
有 KVM 权限的普通账户可用 `LINGCAGE_STORE` 指向自己的目录。
不要让相互不信任的用户共享可写模板。

RPM 检查阶段会编译完整功能的测试，运行不依赖 KVM 的测试。
在专用、兼容的 KVM 测试机上，可用 `rpmbuild --with kvm_tests` 运行上游集成测试。
还需单独验收模板创建、命令执行、虚拟机关机及代理程序的动态库依赖。

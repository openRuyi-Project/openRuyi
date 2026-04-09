# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Chao Liu <chao.liu.riscv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

# Originally extracted from Fedora Project
# Authors: The Fedora Project Contributors

# Default to no KVM support
# kvm_package is only set for architectures that support KVM
%bcond need_qemu_kvm 0
%bcond have_vmsr_helper 0
%ifarch x86_64
%global kvm_package   system-x86
%bcond need_qemu_kvm 1
%bcond have_vmsr_helper 1
%endif

%ifarch riscv64
%global kvm_package   system-riscv
%bcond need_qemu_kvm 1
%endif

# KVM support conditional
%bcond have_kvm 0
%if 0%{?kvm_package:1}
%bcond have_kvm 1
%endif

# modprobe config files
%global modprobe_kvm_conf %{_sourcedir}/kvm.conf
%ifarch x86_64
%global modprobe_kvm_conf %{_sourcedir}/kvm-x86.conf
%endif
%ifarch riscv64
%global modprobe_kvm_conf %{_sourcedir}/kvm-riscv.conf
%endif

# only build QEMU tools package
%bcond tools_only 0

# By default build dynamic user-mode emulation
%bcond user_dynamic 1

# By default do not build static user-mode emulation
%bcond user_static 0

# Disable compiler Werror by default
%bcond enable_werror 0

# Provide a way to skip tests via rpmbuild `--without`
# This makes it easier to skip tests in copr repos, where
# the qemu test suite is historically flakey
%bcond check 0

# Matches xen ExclusiveArch
%bcond have_xen 0

# Matches numactl ExcludeArch
%bcond have_numactl 1

# Matches spice ExclusiveArch
%bcond have_spice 0

# liburing support.
%bcond have_liburing 0

# openRuyi: virtio-gpu not supported yet
%bcond have_virgl 0

# VNC and SDL image and QEMU-UI not supported yet
%bcond have_vnc 0
%bcond have_gvnc_devel 0
%bcond have_sdl_image 0
%bcond have_opengl 0
%bcond have_egl 0
%bcond have_gtk3 0

# openRuyi: persistent memory not supported yet
%bcond have_pmem 0

# openRuyi: QEMU jack audio driver not supported yet
%bcond have_jack 0

# openRuyi: QEMU dbus not supported yet
%bcond have_dbus 0

# openRuyi: block-blkio not supported yet
%bcond have_libblkio 0

# openRuyi: QEMU libcbor not supported yet
%bcond have_libcbor 0

# openRuyi: QEMU brlapi not supported yet
%bcond have_brlapi 0

# openRuyi: QEMU daxctl not supported yet
%bcond have_daxctl 0

# openRuyi: QEMU multipath not supported yet
%bcond have_multipath 0

# openRuyi: QEMU USB not supported yet
%bcond have_usb 0

# openRuyi: QEMU usbredir not supported yet
%bcond have_usbredir 0

# openRuyi: XDP network backend not supported yet
%bcond have_xdp 0

# QEMU Documentation build not supported yet
%bcond have_python3_sphinx 0

# openRuyi: Capstone disassembler not supported yet
%bcond have_capstone 0

# openRuyi: QEMU pipewire not supported yet
%bcond have_pipewire 0

# openRuyi: QEMU keymap not supported yet
%bcond have_cryptodev_backend_lkcf 0
%bcond have_xkb 0

# openRuyi: systemtap and dtrace not supported yet
%bcond have_systemtap 0
%bcond have_dtrace 0

# openRuyi: SLIRP networking backend not supported yet
%bcond have_slirp 0

# openRuyi: QEMU Audio support not ready yet
%bcond have_audio 0

# openRuyi: QEMU dwarf not supported yet
%bcond have_dwarf 0

# openRuyi: QEMU USB support not ready yet
%bcond have_usb 0

# All modules should be listed here.
%bcond have_block_rbd 0

# Not supported on x86_64 and riscv64
%bcond have_block_iscsi 0

# Not supported on x86_64 and riscv64
%bcond have_block_gluster 0

# Not supported on x86_64 and riscv64
%bcond have_block_nfs 0

# Not supported on x86_64 riscv64
%bcond have_librdma 0

# openRuyi: smartcard device not supported yet
%bcond have_libcacard 0

# openRuyi: QEMU rutabaga_gfx not supported yet
%bcond have_rutabaga_gfx 0

# openRuyi: QEMU qatzip not supported yet
%bcond have_qatzip 0

# openRuyi: QEMU igvm not supported yet
%bcond have_igvm 0

# openRuyi: QEMU man not supported yet
%bcond have_man 0

# openRuyi: QEMU fdt default enabled
%bcond have_fdt 1

%global firmwaredirs "%{_datadir}/qemu-firmware:%{_datadir}/ipxe/qemu:%{_datadir}/seavgabios:%{_datadir}/seabios"

%global qemudocdir %{_docdir}/%{name}

Name:           qemu
Version:        10.2.0
Release:        %autorelease
Summary:        Machine emulator and virtualizer
License:        BSD-2-Clause AND BSD-3-Clause AND GPL-2.0-only AND GPL-2.0-or-later AND LGPL-2.1-or-later AND MIT
URL:            http://www.qemu.org/
VCS:            git:https://gitlab.com/qemu-project/qemu
#!RemoteAsset:  sha256:9e30ad1b8b9f7b4463001582d1ab297f39cfccea5d08540c0ca6d6672785883a
Source0:        https://download.qemu.org/%{name}-%{version}.tar.xz
Source1:        qemu-guest-agent.service
Source2:        qemu-ga.sysconfig
Source3:        vhost.conf
Source4:        kvm.conf
Source5:        kvm-x86.conf
Source6:        kvm-riscv.conf
BuildSystem:    autotools

# QEMU RISC-V rvsp-ref upstream patch
Patch1:         0001-target-riscv-cpu.c-remove-bare-condition-for-.profil.patch
Patch2:         0002-target-riscv-Add-server-platform-reference-cpu.patch
Patch3:         0003-hw-riscv-experimental-server-platform-reference-mach.patch
Patch4:         0004-hw-riscv-server_platform_ref.c-add-riscv-iommu-sys.patch
Patch5:         0005-docs-add-rvsp-ref.rst.patch
Patch6:         0006-target-riscv-update-satp_mode-to-SV48-for-rvsp-ref.patch

BuildRequires:  hostname
BuildRequires:  meson
BuildRequires:  bison
BuildRequires:  flex
BuildRequires:  pkgconfig(zlib)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gnutls)
BuildRequires:  pkgconfig(libselinux)
BuildRequires:  cyrus-sasl-devel
BuildRequires:  pkgconfig(libaio)
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(wheel)
%if %{with have_block_iscsi}
BuildRequires:  pkgconfig(libiscsi)
%endif
BuildRequires:  pkgconfig(libattr)
%if %{with have_usb}
BuildRequires:  pkgconfig(libusb-1.0)
%endif
%if %{with have_usbredir}
BuildRequires:  usbredir-devel >= 0.7.1
%endif
%if %{with have_python3_sphinx}
BuildRequires:  python3dist(sphinx)
BuildRequires:  python3dist(sphinx_rtd_theme)
%endif
BuildRequires:  pkgconfig(libseccomp)
# For network block driver
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(libssh)
%if %{with have_block_rbd}
BuildRequires:  librbd-devel
%endif

%if %{with have_systemtap}
# We need both because the 'stap' binary is probed for by configure
BuildRequires:  systemtap
BuildRequires:  systemtap-sdt-devel
BuildRequires:  perl-Test-Harness
%endif
%if %{with have_dtrace}
BuildRequires:  /usr/bin/dtrace
%endif
# For VNC PNG support
BuildRequires:  pkgconfig(libpng)
# For virtiofs
BuildRequires:  pkgconfig(libcap-ng)
# Hard requirement for version >= 1.3
BuildRequires:  pkgconfig(pixman-1)
# For rdma
%if %{with have_librdma}
BuildRequires:  rdma-core-devel
%endif
%if %{with have_fdt}
BuildRequires:  dtc-devel
%endif
# For compressed guest memory dumps
BuildRequires:  pkgconfig(lzo2)
BuildRequires:  snappy-devel
# For NUMA memory binding
%if %{with have_numactl}
BuildRequires:  pkgconfig(numa)
%endif
%if %{with have_multipath}
# qemu-pr-helper multipath support (requires libudev too)
BuildRequires:  multipath-tools
BuildRequires:  pkgconfig(systemd)
%endif
%if %{with have_pmem}
BuildRequires:  pkgconfig(libpmem)
%endif
%if %{with have_xkb}
# qemu-keymap
BuildRequires:  pkgconfig(xkbcommon)
%endif
%if %{with have_opengl}
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(libdrm)
BuildRequires:  pkgconfig(gbm)
%endif
%if %{with have_slirp}
BuildRequires:  pkgconfig(slirp)
%endif
BuildRequires:  pkgconfig(libbpf)
%if %{with have_libblkio}
BuildRequires:  pkgconfig(blkio)
%endif
BuildRequires:  make
%if %{with have_audio}
# -display sdl support
BuildRequires:  pkgconfig(sdl2)
# pulseaudio audio output
BuildRequires:  pkgconfig(libpulse)
%endif
# alsa audio output
BuildRequires:  pkgconfig(alsa)

%if %{with have_block_nfs}
# NFS drive support
BuildRequires:  pkgconfig(libnfs)
%endif
# curses display backend
BuildRequires:  ncurses-devel
%if %{with have_spice}
# spice graphics support
BuildRequires:  pkgconfig(spice-protocol)
BuildRequires:  pkgconfig(spice-server)
%endif
%if %{with have_vnc}
# VNC JPEG support
BuildRequires:  pkgconfig(libjpeg)
%endif
%if %{with have_brlapi}
# Braille device support
BuildRequires:  brlapi-devel
%endif
%if %{with have_block_gluster}
# gluster block driver
BuildRequires:  pkgconfig(glusterfs-api)
%endif
# GTK frontend
%if %{with have_gtk3}
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(vte-2.91)
%endif
# GTK translations
BuildRequires:  gettext
%if %{with have_xen}
# Xen support
BuildRequires:  xen-devel
%endif
# reading bzip2 compressed dmg images
BuildRequires:  pkgconfig(bzip2)
# TLS test suite
BuildRequires:  pkgconfig(libtasn1)
%if %{with have_libcacard}
# smartcard device
BuildRequires:  pkgconfig(libcacard)
%endif
%if %{with have_virgl}
# virgl 3d support
BuildRequires:  pkgconfig(virglrenderer)
%endif
%if %{with have_capstone}
# preferred disassembler for TCG
BuildRequires:  pkgconfig(capstone)
%endif
# qemu-ga
BuildRequires:  pkgconfig(libudev)
# qauth infrastructure
BuildRequires:  pkgconfig(pam)
%if %{with have_liburing}
# liburing support.
BuildRequires:  pkgconfig(liburing)
%endif
# zstd compression support
BuildRequires:  pkgconfig(libzstd)
# `hostname` used by test suite
BuildRequires:  hostname
%if %{with have_daxctl}
# nvdimm dax
BuildRequires:  pkgconfig(libdaxctl)
%endif
%if %{with have_jack}
# jack audio driver
BuildRequires:  (pipewire-jack-audio-connection-kit-devel or jack-audio-connection-kit-devel)
%endif
BuildRequires:  fuse3-devel
%if %{with have_sdl_image}
BuildRequires:  pkgconfig(SDL2_image)
%endif
%if %{with have_gvnc_devel}
# Used by vnc-display-test
BuildRequires:  pkgconfig(gvnc-1.0)
%endif
%if %{with have_pipewire}
# Used by pipewire audio backend
BuildRequires:  pkgconfig(pipewire)
%endif
%if %{with have_cryptodev_backend_lkcf}
# Used by cryptodev-backend-lkcf
BuildRequires:  pkgconfig(libkeyutils)
%endif
%if %{with have_xdp}
# Used by net AF_XDP
BuildRequires:  pkgconfig(libxdp)
%endif
# used by virtio-gpu-rutabaga
%if %{with have_rutabaga_gfx}
BuildRequires:  pkgconfig(rutabaga_gfx_ffi)
%endif
%if %{with have_qatzip}
# --enable-qatzip
BuildRequires:  pkgconfig(qatzip)
%endif
%if %{with have_libcbor}
# --enable-libcbor
BuildRequires:  pkgconfig(libcbor)
%endif
%if %{with have_igvm}
BuildRequires:  igvm-devel
%endif
%if %{with user_static}
BuildRequires:  glib-static
BuildRequires:  glibc-static
BuildRequires:  zlib-devel-static
#BuildRequires:  libatomic-static
%endif
# Requires for the openRuyi 'qemu' metapackage
%if %{with user_dynamic}
Requires:       %{name}-user = %{version}-%{release}
%endif
Requires:       %{name}-system = %{version}-%{release}
Requires:       %{name}-tools = %{version}-%{release}

%description
%{name} is an open source virtualizer that provides hardware
emulation for the KVM hypervisor. %{name} acts as a virtual
machine monitor together with the KVM kernel modules, and emulates the
hardware for a full system such as a PC and its associated peripherals.

%package        docs
Summary:        %{name} documentation
BuildArch:      noarch

%description    docs
%{name}-docs provides documentation files regarding %{name}.

%package        tools
Summary:        %{name} support tools
%if %{with have_systemtap}
Recommends:     systemtap-client
Recommends:     systemtap-devel
%endif
%if %{with have_opengl}
Requires:       mesa-gl
%endif

%description    tools
%{name}-tools provides various tools related to %{name} usage.

%package        tests
Summary:        tests for the %{name} package

%description    tests
The %{name}-tests rpm contains tests that can be used to verify
the functionality of the installed %{name} package

Install this package if you want access to qemu-iotests.
%define testsdir %{_libdir}/%{name}/tests-src

%if %{with user_dynamic}
%package        user
Summary:           QEMU user mode emulation of qemu targets
Requires:          %{name}-user%{?_isa} = %{version}-%{release}

%description    user
This package provides the user mode emulation of qemu targets
%endif

%if %{with user_static}
%package        user-static
Summary:        QEMU user mode emulation of qemu targets static build
Requires(post): systemd-units
Requires(postun): systemd-units
Requires:       qemu-user-static = %{version}-%{release}
Provides:       qemu-user = %{version}-%{release}

%description    user-static
This package provides the user mode emulation of qemu targets built as
static binaries
#endif user_static
%endif

%package        system
Summary:        QEMU system emulator for multi-arch

%description    system
This package provides the QEMU system emulator for multi-arch systems.

%prep
%setup -q -n qemu-%{version}

%global qemu_kvm_build qemu_kvm_build
%global static_builddir static_builddir

mkdir -p %{qemu_kvm_build}
mkdir -p %{static_builddir}

%conf
# nothing to do in %conf

%build
# disable everything except the ones we need
%define disable_everything               \\\
  --audio-drv-list=                      \\\
  --disable-af-xdp                       \\\
  --disable-alsa                         \\\
  --disable-asan                         \\\
  --disable-attr                         \\\
  --disable-auth-pam                     \\\
  --disable-smartcard                    \\\
  --disable-blkio                        \\\
  --disable-block-drv-whitelist-in-tools \\\
  --disable-bochs                        \\\
  --disable-bpf                          \\\
  --disable-brlapi                       \\\
  --disable-bsd-user                     \\\
  --disable-bzip2                        \\\
  --disable-cap-ng                       \\\
  --disable-capstone                     \\\
  --disable-cfi                          \\\
  --disable-cfi-debug                    \\\
  --disable-cloop                        \\\
  --disable-cocoa                        \\\
  --disable-colo-proxy                   \\\
  --disable-coreaudio                    \\\
  --disable-coroutine-pool               \\\
  --disable-crypto-afalg                 \\\
  --disable-curl                         \\\
  --disable-curses                       \\\
  --disable-dbus-display                 \\\
  --disable-debug-graph-lock             \\\
  --disable-debug-info                   \\\
  --disable-debug-mutex                  \\\
  --disable-debug-remap                  \\\
  --disable-debug-tcg                    \\\
  --disable-dmg                          \\\
  --disable-docs                         \\\
  --disable-download                     \\\
  --disable-dsound                       \\\
  --disable-fdt                          \\\
  --disable-fuse                         \\\
  --disable-fuse-lseek                   \\\
  --disable-gcrypt                       \\\
  --disable-gettext                      \\\
  --disable-gio                          \\\
  --disable-glusterfs                    \\\
  --disable-gnutls                       \\\
  --disable-gtk                          \\\
  --disable-gtk-clipboard                \\\
  --disable-guest-agent                  \\\
  --disable-guest-agent-msi              \\\
  --disable-hv-balloon                   \\\
  --disable-hvf                          \\\
  --disable-iconv                        \\\
  --disable-igvm                         \\\
  --disable-jack                         \\\
  --disable-kvm                          \\\
  --disable-l2tpv3                       \\\
  --disable-libcbor                      \\\
  --disable-libdaxctl                    \\\
  --disable-libdw                        \\\
  --disable-libkeyutils                  \\\
  --disable-libiscsi                     \\\
  --disable-libnfs                       \\\
  --disable-libpmem                      \\\
  --disable-libssh                       \\\
  --disable-libudev                      \\\
  --disable-libusb                       \\\
  --disable-linux-aio                    \\\
  --disable-linux-io-uring               \\\
  --disable-linux-user                   \\\
  --disable-lto                          \\\
  --disable-lzfse                        \\\
  --disable-lzo                          \\\
  --disable-malloc-trim                  \\\
  --disable-membarrier                   \\\
  --disable-modules                      \\\
  --disable-module-upgrades              \\\
  --disable-mpath                        \\\
  --disable-multiprocess                 \\\
  --disable-netmap                       \\\
  --disable-nettle                       \\\
  --disable-numa                         \\\
  --disable-nvmm                         \\\
  --disable-opengl                       \\\
  --disable-oss                          \\\
  --disable-pa                           \\\
  --disable-parallels                    \\\
  --disable-passt                        \\\
  --disable-pie                          \\\
  --disable-pipewire                     \\\
  --disable-pixman                       \\\
  --disable-plugins                      \\\
  --disable-pvg                          \\\
  --disable-qcow1                        \\\
  --disable-qed                          \\\
  --disable-qom-cast-debug               \\\
  --disable-qpl                          \\\
  --disable-rbd                          \\\
  --disable-rdma                         \\\
  --disable-relocatable                  \\\
  --disable-replication                  \\\
  --disable-rust                         \\\
  --disable-rutabaga-gfx                 \\\
  --disable-rng-none                     \\\
  --disable-safe-stack                   \\\
  --disable-sdl                          \\\
  --disable-sdl-image                    \\\
  --disable-seccomp                      \\\
  --disable-selinux                      \\\
  --disable-slirp                        \\\
  --disable-slirp-smbd                   \\\
  --disable-smartcard                    \\\
  --disable-snappy                       \\\
  --disable-sndio                        \\\
  --disable-sparse                       \\\
  --disable-spice                        \\\
  --disable-spice-protocol               \\\
  --disable-strict-rust-lints            \\\
  --disable-strip                        \\\
  --disable-system                       \\\
  --disable-tcg                          \\\
  --disable-tools                        \\\
  --disable-tpm                          \\\
  --disable-tsan                         \\\
  --disable-uadk                         \\\
  --disable-u2f                          \\\
  --disable-ubsan                        \\\
  --disable-usb-redir                    \\\
  --disable-user                         \\\
  --disable-valgrind                     \\\
  --disable-vpc                          \\\
  --disable-vde                          \\\
  --disable-vdi                          \\\
  --disable-vfio-user-server             \\\
  --disable-vhdx                         \\\
  --disable-vhost-crypto                 \\\
  --disable-vhost-kernel                 \\\
  --disable-vhost-net                    \\\
  --disable-vhost-user                   \\\
  --disable-vhost-user-blk-server        \\\
  --disable-vhost-vdpa                   \\\
  --disable-virglrenderer                \\\
  --disable-virtfs                       \\\
  --disable-vnc                          \\\
  --disable-vnc-jpeg                     \\\
  --disable-png                          \\\
  --disable-vnc-sasl                     \\\
  --disable-vte                          \\\
  --disable-vvfat                        \\\
  --disable-werror                       \\\
  --disable-whpx                         \\\
  --disable-xen                          \\\
  --disable-xen-pci-passthrough          \\\
  --disable-xkbcommon                    \\\
  --disable-zstd                         \\\
  --without-default-devices

# Starting from version 5.0, QEMU has fully migrated to the Meson
# build system, and its configure script serves merely as a frontend
# wrapper for Meson.
qemu_configure() {
    ../configure                                                 \
        --cc=%{__cc}                                             \
        --cxx=/bin/false                                         \
        --prefix="%{_prefix}"                                    \
        --libdir="%{_libdir}"                                    \
        --datadir="%{_datadir}"                                  \
        --sysconfdir="%{_sysconfdir}"                            \
        --interp-prefix=%{_prefix}/qemu-%M                       \
        --localstatedir="%{_localstatedir}"                      \
        --docdir="%{_docdir}"                                    \
        --libexecdir="%{_libexecdir}"                            \
        --extra-ldflags="%{build_ldflags}"                       \
%ifnarch %{arm}
        --extra-cflags="%{optflags}"                             \
%else
        --extra-cflags="%{optflags} -DSTAP_SDT_ARG_CONSTRAINT=g" \
%endif
        --with-pkgversion="%{name}-%{version}-%{release}"        \
        --with-suffix="%{name}"                                  \
        --firmwarepath="%firmwaredirs"                           \
%if %{with have_dtrace}
        --enable-trace-backends=dtrace                           \
%endif
        --with-coroutine=ucontext                                \
        --tls-priority=@QEMU,SYSTEM                              \
        %{disable_everything}                                    \
        "$@"                                                     \
    || ( cat config.log ; exit 1 )

    echo "config-host.mak contents:"
    echo "==="
    cat config-host.mak
    echo "==="
}

pushd %{qemu_kvm_build}

qemu_configure                                          \
%if %{defined target_list}
  --target-list="%{target_list}"                        \
%endif
%if %{defined block_drivers_rw_list}
  --block-drv-rw-whitelist=%{block_drivers_rw_list}     \
%endif
%if %{defined block_drivers_ro_list}
  --block-drv-ro-whitelist=%{block_drivers_ro_list}     \
%endif
%if %{with have_xdp}
  --enable-af-xdp                                       \
%endif
  --enable-alsa                                         \
  --enable-attr                                         \
%if %{with have_libblkio}
  --enable-blkio                                        \
%endif
  --enable-bpf                                          \
  --enable-cap-ng                                       \
%if %{with have_capstone}
  --enable-capstone                                     \
%endif
  --enable-coroutine-pool                               \
  --enable-curl                                         \
%if %{with have_dbus}
  --enable-dbus-display                                 \
%endif
  --enable-debug-info                                   \
%if %{with have_python3_sphinx}
  --enable-docs                                         \
%endif
  --enable-passt                                        \
%if %{with have_fdt}
  --enable-fdt=system                                   \
%endif
  --enable-gettext                                      \
  --enable-gnutls                                       \
  --enable-guest-agent                                  \
  --enable-iconv                                        \
%if %{with have_igvm}
  --enable-igvm                                         \
%endif
%if %{with have_jack}
  --enable-jack                                         \
%endif
  --enable-kvm                                          \
  --enable-l2tpv3                                       \
%if %{with have_libcbor}
  --enable-libcbor                                      \
%endif
%if %{with have_block_iscsi}
  --enable-libiscsi                                     \
%endif
%if %{with have_pmem}
  --enable-libpmem                                      \
%endif
  --enable-libssh                                       \
%if %{with have_usb}
  --enable-libusb                                       \
%endif
  --enable-libudev                                      \
  --enable-linux-aio                                    \
  --enable-lto                                          \
  --enable-lzo                                          \
  --enable-malloc-trim                                  \
  --enable-modules                                      \
%if %{with have_multipath}
  --enable-mpath                                        \
%endif
%if %{with have_numactl}
  --enable-numa                                         \
%endif
%if %{with have_opengl}
  --enable-opengl                                       \
%endif
  --enable-oss                                          \
  --enable-pie                                          \
%if %{with have_pipewire}
  --enable-pipewire                                     \
%endif
  --enable-pixman                                       \
%if %{with have_block_rbd}
  --enable-rbd                                          \
%endif
  --enable-relocatable                                  \
%if %{with have_librdma}
  --enable-rdma                                         \
%endif
  --enable-seccomp                                      \
  --enable-selinux                                      \
%if %{with have_slirp}
  --enable-slirp                                        \
  --enable-slirp-smbd                                   \
%endif
  --enable-snappy                                       \
  --enable-system                                       \
  --enable-tcg                                          \
  --enable-tools                                        \
  --enable-tpm                                          \
%if %{with have_usbredir}
  --enable-usb-redir                                    \
%endif
  --enable-vhost-kernel                                 \
  --enable-vhost-net                                    \
  --enable-vhost-user                                   \
  --enable-vhost-user-blk-server                        \
  --enable-vhost-vdpa                                   \
  --enable-vnc                                          \
  --enable-png                                          \
  --enable-vnc-sasl                                     \
%if %{with enable_werror}
  --enable-werror                                       \
%endif
%if %{with have_xkb}
  --enable-xkbcommon                                    \
%endif
%if %{with have_audio}
  --enable-sdl                                          \
  --enable-pa                                           \
  --audio-drv-list=pa,pipewire,sdl,alsa,%{?jack_drv}oss \
%else
  --audio-drv-list=alsa,%{?jack_drv}oss                 \
%endif
  --target-list-exclude=moxie-softmmu                   \
  --with-default-devices                                \
  --enable-auth-pam                                     \
  --enable-bochs                                        \
%if %{with have_brlapi}
  --enable-brlapi                                       \
%endif
  --enable-bzip2                                        \
  --enable-cloop                                        \
  --enable-curses                                       \
  --enable-dmg                                          \
  --enable-fuse                                         \
  --enable-gio                                          \
%if %{with have_block_gluster}
  --enable-glusterfs                                    \
%endif
%if %{with have_gtk3}
  --enable-gtk                                          \
%endif
  --enable-hv-balloon                                   \
%if %{with have_daxctl}
  --enable-libdaxctl                                    \
%endif
%if %{with have_dwarf}
  --enable-libdw                                        \
%endif
%if %{with have_cryptodev_backend_lkcf}
  --enable-libkeyutils                                  \
%endif
%if %{with have_block_nfs}
  --enable-libnfs                                       \
%endif
%if %{with have_liburing}
  --enable-linux-io-uring                               \
%endif
%if %{with user_dynamic}
  --enable-linux-user                                   \
%endif
  --enable-multiprocess                                 \
  --enable-parallels                                    \
%if %{with have_qatzip}
  --enable-qatzip                                       \
%endif
  --enable-qcow1                                        \
  --enable-qed                                          \
  --enable-qom-cast-debug                               \
  --enable-replication                                  \
%if %{with have_rutabaga_gfx}
  --enable-rutabaga-gfx                                 \
%endif
%if %{with have_sdl_image}
  --enable-sdl-image                                    \
%endif
%if %{with have_libcacard}
  --enable-smartcard                                    \
%endif
%if %{with have_spice}
  --enable-spice                                        \
  --enable-spice-protocol                               \
%endif
  --enable-vdi                                          \
  --enable-vhost-crypto                                 \
%if %{with have_virgl}
  --enable-virglrenderer                                \
%endif
  --enable-vhdx                                         \
  --enable-virtfs                                       \
  --enable-vpc                                          \
%if %{with have_vnc}
  --enable-vnc-jpeg                                     \
%endif
  --enable-vte                                          \
  --enable-vvfat                                        \
%if %{with have_xen}
  --enable-xen                                          \
%ifarch x86_64
  --enable-xen-pci-passthrough                          \
%endif
%endif
  --enable-zstd

%if %{with tools_only}
%make_build qemu-img
%make_build qemu-io
%make_build qemu-nbd
%make_build storage-daemon/qemu-storage-daemon

%make_build docs/qemu-img.1
%make_build docs/qemu-nbd.8
%make_build docs/qemu-storage-daemon.1
%make_build docs/qemu-storage-daemon-qmp-ref.7

%make_build qga/qemu-ga
%make_build docs/qemu-ga.8

# endif tools_only
%endif

%if !%{with tools_only}
%make_build
popd

# openRuyi build for qemu-user-static
%if %{with user_static}
pushd %{static_builddir}

qemu_configure            \
  --enable-attr           \
  --enable-linux-user     \
  --enable-pie            \
  --enable-tcg            \
  --disable-install-blobs \
  --static

%make_build
popd  # static

%endif

# endif !tools_only
%endif

%install
# Install qemu-guest-agent service and udev rules
install -D -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/qemu-guest-agent.service
install -D -m 0644 %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/qemu-ga

# Install qemu-ga fsfreeze bits
mkdir -p %{buildroot}%{_sysconfdir}/qemu-ga/fsfreeze-hook.d
install -p scripts/qemu-guest-agent/fsfreeze-hook %{buildroot}%{_sysconfdir}/qemu-ga/fsfreeze-hook
mkdir -p %{buildroot}%{_datadir}/%{name}/qemu-ga/fsfreeze-hook.d/
install -p -m 0644 scripts/qemu-guest-agent/fsfreeze-hook.d/*.sample %{buildroot}%{_datadir}/%{name}/qemu-ga/fsfreeze-hook.d/
mkdir -p -v %{buildroot}%{_localstatedir}/log/qemu-ga/

%if %{with tools_only}
pushd %{qemu_kvm_build}
install -D -p -m 0755 qga/qemu-ga %{buildroot}%{_bindir}/qemu-ga
install -D -p -m 0755 qemu-img %{buildroot}%{_bindir}/qemu-img
install -D -p -m 0755 qemu-io %{buildroot}%{_bindir}/qemu-io
install -D -p -m 0755 qemu-nbd %{buildroot}%{_bindir}/qemu-nbd
install -D -p -m 0755 storage-daemon/qemu-storage-daemon %{buildroot}%{_bindir}/qemu-storage-daemon

%if %{with have_man}
mkdir -p %{buildroot}%{_mandir}/man1/
mkdir -p %{buildroot}%{_mandir}/man7/
mkdir -p %{buildroot}%{_mandir}/man8/

install -D -p -m 644 docs/qemu-img.1* %{buildroot}%{_mandir}/man1
install -D -p -m 644 docs/qemu-nbd.8* %{buildroot}%{_mandir}/man8
install -D -p -m 644 docs/qemu-storage-daemon.1* %{buildroot}%{_mandir}/man1
install -D -p -m 644 docs/qemu-storage-daemon-qmp-ref.7* %{buildroot}%{_mandir}/man7
install -D -p -m 644 docs/qemu-ga.8* %{buildroot}%{_mandir}/man8
%endif

popd

# endif tools_only
%endif

%if !%{with tools_only}
# Install qemu-pr-helper service
install -m 0644 contrib/systemd/qemu-pr-helper.service %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/qemu-pr-helper.socket %{buildroot}%{_unitdir}

%if %{with have_vmsr_helper}
# Install qemu-vmsr-helper service
install -m 0644 contrib/systemd/qemu-vmsr-helper.service %{buildroot}%{_unitdir}
install -m 0644 contrib/systemd/qemu-vmsr-helper.socket %{buildroot}%{_unitdir}
%endif

%if %{with have_kvm}
install -D -p -m 0644 %{modprobe_kvm_conf} %{buildroot}%{_sysconfdir}/modprobe.d/kvm.conf
install -D -p -m 0644 %{SOURCE3} %{buildroot}%{_sysconfdir}/modprobe.d/vhost.conf
%endif

# Copy some static data into place
install -D -p -m 0644 -t %{buildroot}%{qemudocdir} README.rst COPYING COPYING.LIB LICENSE docs/interop/qmp-spec.rst
install -D -p -m 0644 qemu.sasl %{buildroot}%{_sysconfdir}/sasl2/%{name}.conf

install -m 0644 scripts/dump-guest-memory.py %{buildroot}%{_datadir}/%{name}

# Install simpletrace
install -m 0755 scripts/simpletrace.py %{buildroot}%{_datadir}/%{name}/simpletrace.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool scripts/tracetool/*.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool/backend
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool/backend scripts/tracetool/backend/*.py
mkdir -p %{buildroot}%{_datadir}/%{name}/tracetool/format
install -m 0644 -t %{buildroot}%{_datadir}/%{name}/tracetool/format scripts/tracetool/format/*.py

# Ensure vhost-user directory is present even if built without virgl
mkdir -p %{buildroot}%{_datadir}/%{name}/vhost-user

# Create new directories and put them all under tests-src
mkdir -p %{buildroot}%{testsdir}/python
mkdir -p %{buildroot}%{testsdir}/tests
mkdir -p %{buildroot}%{testsdir}/tests/qemu-iotests
mkdir -p %{buildroot}%{testsdir}/scripts/qmp

cp -R %{qemu_kvm_build}/python/qemu %{buildroot}%{testsdir}/python
cp -R %{qemu_kvm_build}/scripts/qmp/* %{buildroot}%{testsdir}/scripts/qmp
install -p -m 0755 tests/Makefile.include %{buildroot}%{testsdir}/tests/

# Install qemu-iotests
cp -R tests/qemu-iotests/* %{buildroot}%{testsdir}/tests/qemu-iotests/
cp -ur %{qemu_kvm_build}/tests/qemu-iotests/* %{buildroot}%{testsdir}/tests/qemu-iotests/

# Do the actual qemu tree install
pushd %{qemu_kvm_build}
%make_install

popd

# We need to make the block device modules and other qemu SO files executable
# otherwise RPM won't pick up their dependencies.
chmod +x %{buildroot}%{_libdir}/%{name}/*.so

# Remove docs we don't care about
find %{buildroot}%{qemudocdir} -name .buildinfo -delete
rm -rf %{buildroot}%{qemudocdir}/specs

# Provided by package openbios
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-ppc
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc32
rm -rf %{buildroot}%{_datadir}/%{name}/openbios-sparc64
# Provided by package SLOF
rm -rf %{buildroot}%{_datadir}/%{name}/slof.bin
# Provided by package ipxe
rm -rf %{buildroot}%{_datadir}/%{name}/pxe*rom
rm -rf %{buildroot}%{_datadir}/%{name}/efi*rom
# Provided by package seavgabios
rm -rf %{buildroot}%{_datadir}/%{name}/vgabios*bin
# Provided by package seabios
rm -rf %{buildroot}%{_datadir}/%{name}/bios*.bin
# Provided by ovmf
rm -rf %{buildroot}%{_datadir}/%{name}/edk2*
rm -rf %{buildroot}%{_datadir}/%{name}/firmware

%if %{with have_man}
# Generate qemu-system-* man pages
chmod -x %{buildroot}%{_mandir}/man1/*
for emu in %{buildroot}%{_bindir}/qemu-system-*; do
    ln -sf qemu.1.gz %{buildroot}%{_mandir}/man1/$(basename $emu).1.gz
 done
%endif

# Install kvm specific source bits, and qemu-kvm manpage
%if %{with need_qemu_kvm}
%if %{with have_man}
ln -sf qemu.1.gz %{buildroot}%{_mandir}/man1/qemu-kvm.1.gz
%endif
ln -sf qemu-system-x86_64 %{buildroot}%{_bindir}/qemu-kvm
%endif

# Install binfmt
%if %{with user_dynamic}
%global binfmt_dir %{buildroot}%{_exec_prefix}/lib/binfmt.d
mkdir -p %{binfmt_dir}

%ifarch riscv64
%define ignore_family --ignore-family yes
%endif

./scripts/qemu-binfmt-conf.sh %{?ignore_family} --systemd ALL \
    --exportdir %{binfmt_dir} --qemu-path %{_bindir}
for i in %{binfmt_dir}/*; do mv $i $(echo $i | sed 's/.conf/-dynamic.conf/'); done
%endif

# Install qemu-user-static tree
%if %{with user_static}
%define static_buildroot %{buildroot}/static/
mkdir -p %{static_buildroot}

pushd %{static_builddir}

make DESTDIR=%{static_buildroot} install

# Duplicates what the main build installs and we don't
# need second copy with a -static suffix
rm -f %{static_buildroot}%{_bindir}/qemu-trace-stap

popd  # static

# Rename all QEMU user emulators to have a -static suffix
for src in %{static_buildroot}%{_bindir}/qemu-*; do
    mv $src %{buildroot}%{_bindir}/$(basename $src)-static; done

%if %{with have_systemtap}
# Rename trace files to match -static suffix
for src in %{static_buildroot}%{_datadir}/systemtap/tapset/qemu-*.stp; do
  dst=`echo $src | sed -e 's/.stp/-static.stp/'`
  mv $src $dst
  perl -i -p -e 's/(qemu-\w+)/$1-static/g; s/(qemu\.user\.\w+)/$1.static/g' $dst
  mv $dst %{buildroot}%{_datadir}/systemtap/tapset
 done
%endif

for regularfmt in %{binfmt_dir}/*; do
  staticfmt="$(echo $regularfmt | sed 's/-dynamic/-static/g')"
  cat $regularfmt | tr -d '\n' | sed "s/:$/-static:F/" > $staticfmt
  done

rm -rf %{static_buildroot}
# endif user_static
%endif

# endif !tools_only
%endif

%check

# Disable iotests.
export MTESTARGS="--no-suite block"

# Most architectures can use the default timeouts, but in some cases
# the hardware that's currently available is too slow and we need to
# allow tests to run for a little bit longer
%define timeout_multiplier 1
%ifarch riscv64
%define timeout_multiplier 3
%endif

%if %{with check}
%if !%{with tools_only}
pushd %{qemu_kvm_build}

# Quick sanity check, as it'll give easier to debug failures
# than we see with 'make check'
./qemu-system-x86_64 -help
./qemu-img -help

echo "Testing %{name}-build"

echo "######## unit tests ########"
%make_build check-unit

echo "######## QAPI schema tests ########"
%make_build check-qapi-schema

echo "######## DecodeTree tests ########"
%make_build check-decodetree

echo "######## Soft Float tests ########"
%make_build check-softfloat

echo "######## QTest tests ########"
%make_build check-qtest TIMEOUT_MULTIPLIER=%{timeout_multiplier}

echo "######## Block I/O tests ########"
%make_build check-block TIMEOUT_MULTIPLIER=%{timeout_multiplier}

echo "######## Functional tests ########"
# 'check-func-quick' instead of 'check-functional' to avoid asset download
%make_build check-func-quick TIMEOUT_MULTIPLIER=%{timeout_multiplier}

popd

# endif !tools_only
%endif

# endif with check
%endif

%post -n qemu-tools
%systemd_post qemu-guest-agent.service
%preun -n qemu-tools
%systemd_preun qemu-guest-agent.service
%postun -n qemu-tools
%systemd_postun_with_restart qemu-guest-agent.service

%if !%{with tools_only}

%if %{with user_static}
%post user-static
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :
%postun user-static
/bin/systemctl --system try-restart systemd-binfmt.service &>/dev/null || :
%endif

# endif !tools_only
%endif

%if !%{with tools_only}
%files

%files tools
%if %{with have_xkb}
%{_bindir}/qemu-keymap
%endif
%{_bindir}/qemu-edid
%if %{with have_systemtap}
%{_bindir}/qemu-trace-stap
%endif
%{_datadir}/%{name}/simpletrace.py*
%dir %{_datadir}/%{name}/tracetool/
%{_datadir}/%{name}/tracetool/*.py*
%dir %{_datadir}/%{name}/tracetool/backend/
%{_datadir}/%{name}/tracetool/backend/*.py*
%dir %{_datadir}/%{name}/tracetool/format/
%{_datadir}/%{name}/tracetool/format/*.py*
%{_datadir}/%{name}/dump-guest-memory.py*
%{_datadir}/%{name}/trace-events-all
%if %{with have_man AND have_systemtap}
%{_mandir}/man1/qemu-trace-stap.1*
%endif
%{_bindir}/elf2dmp
%{_bindir}/qemu-pr-helper
%{_unitdir}/qemu-pr-helper.service
%{_unitdir}/qemu-pr-helper.socket
%if %{with have_man}
%{_mandir}/man8/qemu-pr-helper.8*
%endif
%doc COPYING README.rst
%{_bindir}/qemu-ga
%{_unitdir}/qemu-guest-agent.service
%if %{with have_man}
%{_mandir}/man8/qemu-ga.8*
%endif
%config(noreplace) %{_sysconfdir}/sysconfig/qemu-ga
%{_sysconfdir}/qemu-ga
%{_datadir}/%{name}/qemu-ga
%dir %{_localstatedir}/log/qemu-ga
%{_bindir}/qemu-img
%{_bindir}/qemu-io
%{_bindir}/qemu-nbd
%{_bindir}/qemu-storage-daemon
%if %{with have_man}
%{_mandir}/man1/qemu-img.1*
%{_mandir}/man8/qemu-nbd.8*
%{_mandir}/man1/qemu-storage-daemon.1*
%{_mandir}/man7/qemu-storage-daemon-qmp-ref.7*
%endif
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-img.stp
%{_datadir}/systemtap/tapset/qemu-img-log.stp
%{_datadir}/systemtap/tapset/qemu-img-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-io.stp
%{_datadir}/systemtap/tapset/qemu-io-log.stp
%{_datadir}/systemtap/tapset/qemu-io-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-nbd.stp
%{_datadir}/systemtap/tapset/qemu-nbd-log.stp
%{_datadir}/systemtap/tapset/qemu-nbd-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-storage-daemon.stp
%{_datadir}/systemtap/tapset/qemu-storage-daemon-log.stp
%{_datadir}/systemtap/tapset/qemu-storage-daemon-simpletrace.stp
%endif
%if %{with have_libblkio}
%{_libdir}/%{name}/block-blkio.so
%endif
%{_libdir}/%{name}/block-curl.so
%if %{with have_block_iscsi}
%{_libdir}/%{name}/block-iscsi.so
%endif
%if %{with have_block_rbd}
%{_libdir}/%{name}/block-rbd.so
%endif
%{_libdir}/%{name}/block-ssh.so
%if %{with have_opengl}
%{_libdir}/%{name}/ui-opengl.so
%endif
%{_libdir}/%{name}/block-dmg-bz2.so
%if %{with have_block_gluster}
%{_libdir}/%{name}/block-gluster.so
%endif
%if %{with have_block_nfs}
%{_libdir}/%{name}/block-nfs.so
%endif
%{_libdir}/%{name}/audio-alsa.so
%if %{with have_dbus}
%{_libdir}/%{name}/audio-dbus.so
%endif
%{_libdir}/%{name}/audio-oss.so
%if %{with have_audio}
%{_libdir}/%{name}/audio-pa.so
%endif
%if %{with have_pipewire}
%{_libdir}/%{name}/audio-pipewire.so
%endif
%if %{with have_audio}
%{_libdir}/%{name}/audio-sdl.so
%endif
%if %{with have_jack}
%{_libdir}/%{name}/audio-jack.so
%endif
%{_libdir}/%{name}/ui-curses.so
%if %{with have_dbus}
%{_libdir}/%{name}/ui-dbus.so
%endif
%if %{with have_gtk3}
%{_libdir}/%{name}/ui-gtk.so
%endif
%if %{with have_sdl_image}
%{_libdir}/%{name}/ui-sdl.so
%endif
%if %{with have_egl}
%{_libdir}/%{name}/ui-egl-headless.so
%endif
%if %{with have_brlapi}
%{_libdir}/%{name}/chardev-baum.so
%endif
%{_libdir}/%{name}/hw-display-virtio-gpu.so
%if %{with have_virgl}
%{_libdir}/%{name}/hw-display-virtio-gpu-gl.so
%endif
%if %{with have_rutabaga_gfx}
%{_libdir}/%{name}/hw-display-virtio-gpu-rutabaga.so
%endif
%{_libdir}/%{name}/hw-display-virtio-gpu-pci.so
%if %{with have_virgl}
%{_libdir}/%{name}/hw-display-virtio-gpu-pci-gl.so
%endif
%if %{with have_rutabaga_gfx}
%{_libdir}/%{name}/hw-display-virtio-gpu-pci-rutabaga.so
%endif
%{_libdir}/%{name}/hw-s390x-virtio-gpu-ccw.so
%{_libdir}/%{name}/hw-display-virtio-vga.so
%if %{with have_virgl}
%{_libdir}/%{name}/hw-display-virtio-vga-gl.so
%endif
%if %{with have_rutabaga_gfx}
%{_libdir}/%{name}/hw-display-virtio-vga-rutabaga.so
%endif
%{_libdir}/%{name}/hw-uefi-vars.so
%if %{with have_usb}
%{_libdir}/%{name}/hw-usb-host.so
%{_libdir}/%{name}/hw-usb-redirect.so
%endif
%if %{with have_libcacard}
%{_libdir}/%{name}/hw-usb-smartcard.so
%endif
%if %{with have_virgl}
%{_datadir}/%{name}/vhost-user/50-qemu-gpu.json
%{_libexecdir}/vhost-user-gpu
%endif
%if %{with have_spice}
%{_libdir}/%{name}/audio-spice.so
%{_libdir}/%{name}/chardev-spice.so
%{_libdir}/%{name}/hw-display-qxl.so
%{_libdir}/%{name}/ui-spice-core.so
%{_libdir}/%{name}/ui-spice-app.so
%endif
%dir %{_datadir}/%{name}/
%dir %{_datadir}/%{name}/dtb/
%dir %{_datadir}/%{name}/vhost-user/
%{_datadir}/icons/*
%{_datadir}/%{name}/keymaps/
%{_datadir}/%{name}/linuxboot_dma.bin
%attr(4755, -, -) %{_libexecdir}/qemu-bridge-helper
%dir %{_libdir}/%{name}/
%if %{with have_man}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man7/qemu-block-drivers.7*
%{_mandir}/man7/qemu-cpu-models.7*
%{_mandir}/man7/qemu-ga-ref.7*
%{_mandir}/man7/qemu-qmp-ref.7*
%endif
%if %{with have_kvm}
%config(noreplace) %{_sysconfdir}/modprobe.d/kvm.conf
%config(noreplace) %{_sysconfdir}/modprobe.d/vhost.conf
%endif
%config(noreplace) %{_sysconfdir}/sasl2/%{name}.conf
%{_datadir}/applications/qemu.desktop
%exclude %{_datadir}/%{name}/qemu-nsis.bmp

%files docs
%doc %{qemudocdir}

%files tests
%{testsdir}
%{_libdir}/%{name}/accel-qtest-*.so

%if %{with user_dynamic}
%files user
%{_bindir}/qemu-i386
%{_bindir}/qemu-arm
%{_bindir}/qemu-armeb
%{_bindir}/qemu-hexagon
%{_bindir}/qemu-m68k
%{_bindir}/qemu-microblaze
%{_bindir}/qemu-microblazeel
%{_bindir}/qemu-mips
%{_bindir}/qemu-mipsel
%{_bindir}/qemu-or1k
%{_bindir}/qemu-ppc
%{_bindir}/qemu-riscv32
%{_bindir}/qemu-sh4
%{_bindir}/qemu-sh4eb
%{_bindir}/qemu-sparc
%{_bindir}/qemu-xtensa
%{_bindir}/qemu-xtensaeb
%{_bindir}/qemu-x86_64
%{_bindir}/qemu-aarch64
%{_bindir}/qemu-aarch64_be
%{_bindir}/qemu-alpha
%{_bindir}/qemu-hppa
%{_bindir}/qemu-loongarch64
%{_bindir}/qemu-mips64
%{_bindir}/qemu-mips64el
%{_bindir}/qemu-mipsn32
%{_bindir}/qemu-mipsn32el
%{_bindir}/qemu-ppc64
%{_bindir}/qemu-ppc64le
%{_bindir}/qemu-riscv64
%{_bindir}/qemu-s390x
%{_bindir}/qemu-sparc32plus
%{_bindir}/qemu-sparc64
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-armeb.stp
%{_datadir}/systemtap/tapset/qemu-armeb-log.stp
%{_datadir}/systemtap/tapset/qemu-armeb-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-arm.stp
%{_datadir}/systemtap/tapset/qemu-arm-log.stp
%{_datadir}/systemtap/tapset/qemu-arm-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-hexagon.stp
%{_datadir}/systemtap/tapset/qemu-hexagon-log.stp
%{_datadir}/systemtap/tapset/qemu-hexagon-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-m68k.stp
%{_datadir}/systemtap/tapset/qemu-m68k-log.stp
%{_datadir}/systemtap/tapset/qemu-m68k-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-microblaze.stp
%{_datadir}/systemtap/tapset/qemu-microblaze-log.stp
%{_datadir}/systemtap/tapset/qemu-microblaze-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel-log.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mips.stp
%{_datadir}/systemtap/tapset/qemu-mips-log.stp
%{_datadir}/systemtap/tapset/qemu-mips-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mipsel.stp
%{_datadir}/systemtap/tapset/qemu-mipsel-log.stp
%{_datadir}/systemtap/tapset/qemu-mipsel-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-or1k.stp
%{_datadir}/systemtap/tapset/qemu-or1k-log.stp
%{_datadir}/systemtap/tapset/qemu-or1k-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-ppc.stp
%{_datadir}/systemtap/tapset/qemu-ppc-log.stp
%{_datadir}/systemtap/tapset/qemu-ppc-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-riscv32.stp
%{_datadir}/systemtap/tapset/qemu-riscv32-log.stp
%{_datadir}/systemtap/tapset/qemu-riscv32-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-sh4.stp
%{_datadir}/systemtap/tapset/qemu-sh4-log.stp
%{_datadir}/systemtap/tapset/qemu-sh4-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb-log.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-sparc.stp
%{_datadir}/systemtap/tapset/qemu-sparc-log.stp
%{_datadir}/systemtap/tapset/qemu-sparc-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-xtensa.stp
%{_datadir}/systemtap/tapset/qemu-xtensa-log.stp
%{_datadir}/systemtap/tapset/qemu-xtensa-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb-log.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-aarch64.stp
%{_datadir}/systemtap/tapset/qemu-aarch64-log.stp
%{_datadir}/systemtap/tapset/qemu-aarch64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be-log.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-alpha.stp
%{_datadir}/systemtap/tapset/qemu-alpha-log.stp
%{_datadir}/systemtap/tapset/qemu-alpha-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-hppa.stp
%{_datadir}/systemtap/tapset/qemu-hppa-log.stp
%{_datadir}/systemtap/tapset/qemu-hppa-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64-log.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mips64el.stp
%{_datadir}/systemtap/tapset/qemu-mips64el-log.stp
%{_datadir}/systemtap/tapset/qemu-mips64el-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mips64.stp
%{_datadir}/systemtap/tapset/qemu-mips64-log.stp
%{_datadir}/systemtap/tapset/qemu-mips64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32-log.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el-log.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-ppc64.stp
%{_datadir}/systemtap/tapset/qemu-ppc64-log.stp
%{_datadir}/systemtap/tapset/qemu-ppc64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le-log.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-riscv64.stp
%{_datadir}/systemtap/tapset/qemu-riscv64-log.stp
%{_datadir}/systemtap/tapset/qemu-riscv64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-s390x.stp
%{_datadir}/systemtap/tapset/qemu-s390x-log.stp
%{_datadir}/systemtap/tapset/qemu-s390x-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus-log.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-sparc64.stp
%{_datadir}/systemtap/tapset/qemu-sparc64-log.stp
%{_datadir}/systemtap/tapset/qemu-sparc64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-x86_64.stp
%{_datadir}/systemtap/tapset/qemu-x86_64-log.stp
%{_datadir}/systemtap/tapset/qemu-x86_64-simpletrace.stp
# endif !have_systemtap
%endif
%{_exec_prefix}/lib/binfmt.d/qemu-*-dynamic.conf
%endif

%if %{with user_static}
%files user-static
%license COPYING COPYING.LIB LICENSE
%{_bindir}/qemu-aarch64-static
%{_bindir}/qemu-aarch64_be-static
%{_bindir}/qemu-alpha-static
%{_bindir}/qemu-hppa-static
%{_bindir}/qemu-loongarch64-static
%{_bindir}/qemu-mips64-static
%{_bindir}/qemu-mips64el-static
%{_bindir}/qemu-mipsn32-static
%{_bindir}/qemu-mipsn32el-static
%{_bindir}/qemu-ppc64-static
%{_bindir}/qemu-ppc64le-static
%{_bindir}/qemu-riscv64-static
%{_bindir}/qemu-s390x-static
%{_bindir}/qemu-sparc32plus-static
%{_bindir}/qemu-sparc64-static
%{_bindir}/qemu-x86_64-static
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-aarch64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-aarch64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-aarch64-static.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be-log-static.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-aarch64_be-static.stp
%{_datadir}/systemtap/tapset/qemu-alpha-log-static.stp
%{_datadir}/systemtap/tapset/qemu-alpha-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-alpha-static.stp
%{_datadir}/systemtap/tapset/qemu-hppa-log-static.stp
%{_datadir}/systemtap/tapset/qemu-hppa-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-hppa-static.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-loongarch64-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64el-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64el-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mips64el-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsn32el-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le-log-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc64le-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv64-static.stp
%{_datadir}/systemtap/tapset/qemu-s390x-log-static.stp
%{_datadir}/systemtap/tapset/qemu-s390x-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-s390x-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc64-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus-log-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc32plus-static.stp
%{_datadir}/systemtap/tapset/qemu-x86_64-log-static.stp
%{_datadir}/systemtap/tapset/qemu-x86_64-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-x86_64-static.stp
%endif
%{_exec_prefix}/lib/binfmt.d/qemu-aarch64-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-aarch64_be-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-alpha-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-hppa-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-loongarch64-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mips64-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mips64el-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mipsn32-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mipsn32el-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-ppc64-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-ppc64le-static.conf
%ifnarch riscv64
%{_exec_prefix}/lib/binfmt.d/qemu-riscv64-static.conf
%endif
%ifnarch x86_64
%{_exec_prefix}/lib/binfmt.d/qemu-x86_64-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-i486-static.conf
%endif
%{_exec_prefix}/lib/binfmt.d/qemu-s390x-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-sparc32plus-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-sparc64-static.conf
%{_bindir}/qemu-arm-static
%{_bindir}/qemu-armeb-static
%{_bindir}/qemu-hexagon-static
%{_bindir}/qemu-m68k-static
%{_bindir}/qemu-microblaze-static
%{_bindir}/qemu-microblazeel-static
%{_bindir}/qemu-mips-static
%{_bindir}/qemu-mipsel-static
%{_bindir}/qemu-or1k-static
%{_bindir}/qemu-ppc-static
%{_bindir}/qemu-riscv32-static
%{_bindir}/qemu-sh4-static
%{_bindir}/qemu-sh4eb-static
%{_bindir}/qemu-sparc-static
%{_bindir}/qemu-xtensa-static
%{_bindir}/qemu-xtensaeb-static
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-arm-log-static.stp
%{_datadir}/systemtap/tapset/qemu-arm-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-arm-static.stp
%{_datadir}/systemtap/tapset/qemu-armeb-log-static.stp
%{_datadir}/systemtap/tapset/qemu-armeb-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-armeb-static.stp
%{_datadir}/systemtap/tapset/qemu-hexagon-log-static.stp
%{_datadir}/systemtap/tapset/qemu-hexagon-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-hexagon-static.stp
%{_datadir}/systemtap/tapset/qemu-m68k-log-static.stp
%{_datadir}/systemtap/tapset/qemu-m68k-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-m68k-static.stp
%{_datadir}/systemtap/tapset/qemu-microblaze-log-static.stp
%{_datadir}/systemtap/tapset/qemu-microblaze-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-microblaze-static.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel-log-static.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-microblazeel-static.stp
%{_datadir}/systemtap/tapset/qemu-mips-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mips-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mips-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsel-log-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsel-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-mipsel-static.stp
%{_datadir}/systemtap/tapset/qemu-or1k-log-static.stp
%{_datadir}/systemtap/tapset/qemu-or1k-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-or1k-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc-log-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-ppc-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv32-log-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv32-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-riscv32-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4-log-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb-log-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-sh4eb-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc-log-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-sparc-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensa-log-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensa-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensa-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb-log-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb-simpletrace-static.stp
%{_datadir}/systemtap/tapset/qemu-xtensaeb-static.stp
%endif
%{_exec_prefix}/lib/binfmt.d/qemu-arm-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-armeb-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-hexagon-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-m68k-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-microblaze-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-microblazeel-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mips-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-mipsel-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-or1k-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-ppc-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-riscv32-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-sh4-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-sh4eb-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-sparc-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-xtensa-static.conf
%{_exec_prefix}/lib/binfmt.d/qemu-xtensaeb-static.conf

#endif %{user_static}
%endif

%files system
%{_bindir}/qemu-system-aarch64
%{_bindir}/qemu-system-alpha
%{_bindir}/qemu-system-hppa
%{_bindir}/qemu-system-loongarch64
%{_bindir}/qemu-system-mips64
%{_bindir}/qemu-system-mips64el
%{_bindir}/qemu-system-ppc64
%{_bindir}/qemu-system-riscv64
%{_bindir}/qemu-system-s390x
%{_bindir}/qemu-system-sparc64
%{_bindir}/qemu-system-x86_64
%{_datadir}/%{name}/palcode-clipper
%{_datadir}/%{name}/hppa-firmware.img
%{_datadir}/%{name}/hppa-firmware64.img
%{_datadir}/%{name}/s390-ccw.img
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-system-aarch64.stp
%{_datadir}/systemtap/tapset/qemu-system-aarch64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-aarch64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-alpha.stp
%{_datadir}/systemtap/tapset/qemu-system-alpha-log.stp
%{_datadir}/systemtap/tapset/qemu-system-alpha-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-hppa.stp
%{_datadir}/systemtap/tapset/qemu-system-hppa-log.stp
%{_datadir}/systemtap/tapset/qemu-system-hppa-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-loongarch64.stp
%{_datadir}/systemtap/tapset/qemu-system-loongarch64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-loongarch64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64el.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64el-log.stp
%{_datadir}/systemtap/tapset/qemu-system-mips64el-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc64.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv64.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-s390x.stp
%{_datadir}/systemtap/tapset/qemu-system-s390x-log.stp
%{_datadir}/systemtap/tapset/qemu-system-s390x-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc64.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc64-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-x86_64.stp
%{_datadir}/systemtap/tapset/qemu-system-x86_64-log.stp
%{_datadir}/systemtap/tapset/qemu-system-x86_64-simpletrace.stp
%endif
%if %{with have_man}
%{_mandir}/man1/qemu-system-aarch64.1*
%{_mandir}/man1/qemu-system-alpha.1*
%{_mandir}/man1/qemu-system-hppa.1*
%{_mandir}/man1/qemu-system-loongarch64.1*
%{_mandir}/man1/qemu-system-m68k.1*
%{_mandir}/man1/qemu-system-mips64el.1*
%{_mandir}/man1/qemu-system-mips64.1*
%{_mandir}/man1/qemu-system-or1k.1*
%{_mandir}/man1/qemu-system-ppc.1*
%{_mandir}/man1/qemu-system-ppc64.1*
%{_mandir}/man1/qemu-system-riscv*.1*
%{_mandir}/man1/qemu-system-rx.1*
%{_mandir}/man1/qemu-system-s390x.1*
%{_mandir}/man1/qemu-system-sparc64.1*
%{_mandir}/man1/qemu-system-x86_64.1*
%endif
%{_bindir}/qemu-system-arm
%{_bindir}/qemu-system-avr
%{_bindir}/qemu-system-m68k
%{_bindir}/qemu-system-microblaze
%{_bindir}/qemu-system-microblazeel
%{_bindir}/qemu-system-mips
%{_bindir}/qemu-system-mipsel
%{_bindir}/qemu-system-or1k
%{_bindir}/qemu-system-ppc
%{_bindir}/qemu-system-riscv32
%{_bindir}/qemu-system-rx
%{_bindir}/qemu-system-sh4
%{_bindir}/qemu-system-sh4eb
%{_bindir}/qemu-system-sparc
%{_bindir}/qemu-system-tricore
%{_bindir}/qemu-system-i386
%{_bindir}/qemu-system-xtensa
%{_bindir}/qemu-system-xtensaeb
%{_datadir}/%{name}/dtb/bamboo.dtb
%{_datadir}/%{name}/dtb/canyonlands.dtb
%{_datadir}/%{name}/dtb/pegasos1.dtb
%{_datadir}/%{name}/dtb/pegasos2.dtb
%{_datadir}/%{name}/qemu_vga.ndrv
%{_datadir}/%{name}/pnv-pnor.bin
%{_datadir}/%{name}/skiboot.lid
%{_datadir}/%{name}/u-boot.e500
%{_datadir}/%{name}/u-boot-sam460.bin
%{_datadir}/%{name}/vof*.bin
%{_datadir}/%{name}/dtb/petalogix*.dtb
%{_datadir}/%{name}/opensbi-riscv*.bin
%{_datadir}/%{name}/ast27x0_bootrom.bin
%{_datadir}/%{name}/npcm7xx_bootrom.bin
%{_datadir}/%{name}/npcm8xx_bootrom.bin
%{_datadir}/%{name}/QEMU,tcx.bin
%{_datadir}/%{name}/QEMU,cgthree.bin
%{_datadir}/%{name}/kvmvapic.bin
%{_datadir}/%{name}/linuxboot.bin
%{_datadir}/%{name}/multiboot.bin
%{_datadir}/%{name}/multiboot_dma.bin
%{_datadir}/%{name}/pvh.bin
%{_datadir}/%{name}/qboot.rom
%if %{with have_vmsr_helper}
%{_bindir}/qemu-vmsr-helper
%{_unitdir}/qemu-vmsr-helper.service
%{_unitdir}/qemu-vmsr-helper.socket
%endif
%if %{with need_qemu_kvm}
%{_bindir}/qemu-kvm
%endif
%if %{with have_systemtap}
%{_datadir}/systemtap/tapset/qemu-system-arm.stp
%{_datadir}/systemtap/tapset/qemu-system-arm-log.stp
%{_datadir}/systemtap/tapset/qemu-system-arm-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-avr.stp
%{_datadir}/systemtap/tapset/qemu-system-avr-log.stp
%{_datadir}/systemtap/tapset/qemu-system-avr-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-m68k.stp
%{_datadir}/systemtap/tapset/qemu-system-m68k-log.stp
%{_datadir}/systemtap/tapset/qemu-system-m68k-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-microblaze.stp
%{_datadir}/systemtap/tapset/qemu-system-microblaze-log.stp
%{_datadir}/systemtap/tapset/qemu-system-microblaze-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-microblazeel.stp
%{_datadir}/systemtap/tapset/qemu-system-microblazeel-log.stp
%{_datadir}/systemtap/tapset/qemu-system-microblazeel-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-mips.stp
%{_datadir}/systemtap/tapset/qemu-system-mips-log.stp
%{_datadir}/systemtap/tapset/qemu-system-mips-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-mipsel.stp
%{_datadir}/systemtap/tapset/qemu-system-mipsel-log.stp
%{_datadir}/systemtap/tapset/qemu-system-mipsel-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-or1k.stp
%{_datadir}/systemtap/tapset/qemu-system-or1k-log.stp
%{_datadir}/systemtap/tapset/qemu-system-or1k-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc-log.stp
%{_datadir}/systemtap/tapset/qemu-system-ppc-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv32.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv32-log.stp
%{_datadir}/systemtap/tapset/qemu-system-riscv32-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-rx.stp
%{_datadir}/systemtap/tapset/qemu-system-rx-log.stp
%{_datadir}/systemtap/tapset/qemu-system-rx-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4-log.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4eb.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4eb-log.stp
%{_datadir}/systemtap/tapset/qemu-system-sh4eb-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc-log.stp
%{_datadir}/systemtap/tapset/qemu-system-sparc-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-tricore.stp
%{_datadir}/systemtap/tapset/qemu-system-tricore-log.stp
%{_datadir}/systemtap/tapset/qemu-system-tricore-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-i386.stp
%{_datadir}/systemtap/tapset/qemu-system-i386-log.stp
%{_datadir}/systemtap/tapset/qemu-system-i386-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensa.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensa-log.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensa-simpletrace.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensaeb.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensaeb-log.stp
%{_datadir}/systemtap/tapset/qemu-system-xtensaeb-simpletrace.stp
%endif
%if %{with have_man}
%{_mandir}/man1/qemu-system-alpha.1*
%{_mandir}/man1/qemu-system-arm.1*
%{_mandir}/man1/qemu-system-avr.1*
%{_mandir}/man1/qemu-system-hppa.1*
%{_mandir}/man1/qemu-system-m68k.1*
%{_mandir}/man1/qemu-system-microblaze.1*
%{_mandir}/man1/qemu-system-microblazeel.1*
%{_mandir}/man1/qemu-system-mips.1*
%{_mandir}/man1/qemu-system-mipsel.1*
%{_mandir}/man1/qemu-system-mips64el.1*
%{_mandir}/man1/qemu-system-mips64.1*
%{_mandir}/man1/qemu-system-or1k.1*
%{_mandir}/man1/qemu-system-ppc.1*
%{_mandir}/man1/qemu-system-riscv*.1*
%{_mandir}/man1/qemu-system-rx.1*
%{_mandir}/man1/qemu-system-sh4.1*
%{_mandir}/man1/qemu-system-sh4eb.1*
%{_mandir}/man1/qemu-system-sparc.1*
%{_mandir}/man1/qemu-system-tricore.1*
%{_mandir}/man1/qemu-system-i386.1*
%{_mandir}/man1/qemu-system-xtensa.1*
%{_mandir}/man1/qemu-system-xtensaeb.1*
%if %{with need_qemu_kvm}
%{_mandir}/man1/qemu-kvm.1*
%endif
%endif

# endif !tools_only
%endif

%changelog
%autochangelog

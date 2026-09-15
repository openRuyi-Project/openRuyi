# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name lingcore
%global full_version 0.2.0
%global pkgname lingcore-0.2

Name:           rust-lingcore-0.2
Version:        0.2.0
Release:        %autorelease
Summary:        Rust crate "lingcore"
License:        Apache-2.0
URL:            https://lingcage.com
#!RemoteAsset:  sha256:a813a741ec85e08e4bf187820a7d961c5ec8440ab4e3f7391c6ca2a88a465d91
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.29
Requires:       crate(thiserror-2/default) >= 2.0.18

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for the Rust crate "lingcore"

%package     -n %{name}+acpi
Summary:        Building blocks for agentic-workload VMMs - feature "acpi"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mem) = %{version}
Requires:       crate(acpi-tables-0.2/default) >= 0.2.1
Provides:       crate(%{pkgname}/acpi) = %{version}

%description -n %{name}+acpi
This metapackage enables feature "acpi" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+boot
Summary:        Building blocks for agentic-workload VMMs - feature "boot"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hv) = %{version}
Requires:       crate(%{pkgname}/mem) = %{version}
Requires:       crate(linux-loader-0.14/bzimage) >= 0.14.0
Provides:       crate(%{pkgname}/boot) = %{version}

%description -n %{name}+boot
This metapackage enables feature "boot" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cli
Summary:        Building blocks for agentic-workload VMMs - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kvm) = %{version}
Requires:       crate(%{pkgname}/machine) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+devices
Summary:        Building blocks for agentic-workload VMMs - feature "devices"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/vcpu) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Provides:       crate(%{pkgname}/devices) = %{version}

%description -n %{name}+devices
This metapackage enables feature "devices" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fdt
Summary:        Building blocks for agentic-workload VMMs - feature "fdt"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mem) = %{version}
Requires:       crate(vm-fdt-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/fdt) = %{version}

%description -n %{name}+fdt
This metapackage enables feature "fdt" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+hv
Summary:        Building blocks for agentic-workload VMMs - feature "hv" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/hv) = %{version}
Provides:       crate(%{pkgname}/vcpu) = %{version}

%description -n %{name}+hv
This metapackage enables feature "hv" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default", and "vcpu" features.

%package     -n %{name}+kvm
Summary:        Building blocks for agentic-workload VMMs - feature "kvm"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/hv) = %{version}
Requires:       crate(kvm-bindings-0.14/default) >= 0.14.1
Requires:       crate(kvm-ioctls-0.25/default) >= 0.25.0
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Requires:       crate(serde-json-1/default) >= 1.0.149
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/kvm) = %{version}

%description -n %{name}+kvm
This metapackage enables feature "kvm" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+machine
Summary:        Building blocks for agentic-workload VMMs - feature "machine"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/acpi) = %{version}
Requires:       crate(%{pkgname}/boot) = %{version}
Requires:       crate(%{pkgname}/devices) = %{version}
Requires:       crate(%{pkgname}/fdt) = %{version}
Requires:       crate(%{pkgname}/hv) = %{version}
Requires:       crate(%{pkgname}/mem) = %{version}
Requires:       crate(%{pkgname}/netstack) = %{version}
Requires:       crate(%{pkgname}/seccomp) = %{version}
Requires:       crate(%{pkgname}/serde) = %{version}
Requires:       crate(%{pkgname}/vcpu) = %{version}
Requires:       crate(%{pkgname}/virtio) = %{version}
Provides:       crate(%{pkgname}/machine) = %{version}

%description -n %{name}+machine
This metapackage enables feature "machine" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mem
Summary:        Building blocks for agentic-workload VMMs - feature "mem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(vm-memory-0.18/backend-mmap) >= 0.18.0
Requires:       crate(vm-memory-0.18/default) >= 0.18.0
Provides:       crate(%{pkgname}/mem) = %{version}

%description -n %{name}+mem
This metapackage enables feature "mem" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+netstack
Summary:        Building blocks for agentic-workload VMMs - feature "netstack"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/virtio) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(smoltcp-0.13/auto-icmp-echo-reply) >= 0.13.1
Requires:       crate(smoltcp-0.13/medium-ethernet) >= 0.13.1
Requires:       crate(smoltcp-0.13/proto-dhcpv4) >= 0.13.1
Requires:       crate(smoltcp-0.13/proto-ipv4) >= 0.13.1
Requires:       crate(smoltcp-0.13/socket-tcp) >= 0.13.1
Requires:       crate(smoltcp-0.13/socket-udp) >= 0.13.1
Requires:       crate(smoltcp-0.13/std) >= 0.13.1
Provides:       crate(%{pkgname}/netstack) = %{version}

%description -n %{name}+netstack
This metapackage enables feature "netstack" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+seccomp
Summary:        Building blocks for agentic-workload VMMs - feature "seccomp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libc-0.2/default) >= 0.2.180
Requires:       crate(seccompiler-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/seccomp) = %{version}

%description -n %{name}+seccomp
This metapackage enables feature "seccomp" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+serde
Summary:        Building blocks for agentic-workload VMMs - feature "serde"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(serde-1/default) >= 1.0.228
Requires:       crate(serde-1/derive) >= 1.0.228
Provides:       crate(%{pkgname}/serde) = %{version}

%description -n %{name}+serde
This metapackage enables feature "serde" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+virtio
Summary:        Building blocks for agentic-workload VMMs - feature "virtio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/devices) = %{version}
Requires:       crate(%{pkgname}/mem) = %{version}
Provides:       crate(%{pkgname}/virtio) = %{version}

%description -n %{name}+virtio
This metapackage enables feature "virtio" for the Rust lingcore crate, by pulling in any additional dependencies needed by that feature.

%files
%license LICENSE
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

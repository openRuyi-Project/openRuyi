# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name vfio-ioctls
%global full_version 0.6.0
%global pkgname vfio-ioctls-0.6

Name:           rust-vfio-ioctls-0.6
Version:        0.6.0
Release:        %autorelease
Summary:        Rust crate "vfio-ioctls"
License:        Apache-2.0 OR BSD-3-Clause
URL:            https://github.com/rust-vmm/vfio
#!RemoteAsset:  sha256:d4b1d98dff7f0d219278e406323e7eda4d426447bd203c7828189baf0d8c07b7
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(byteorder-1/default) >= 1.2.1
Requires:       crate(libc-0.2/default) >= 0.2.39
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(thiserror-2/default) >= 2.0.16
Requires:       crate(vfio-bindings-0.6/default) >= 0.6.2
Requires:       crate(vm-memory-0.16/backend-mmap) >= 0.16.0
Requires:       crate(vm-memory-0.16/default) >= 0.16.0
Requires:       crate(vmm-sys-util-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "vfio-ioctls"

%package     -n %{name}+iommufd-bindings
Summary:        Safe wrappers over VFIO ioctls - feature "iommufd-bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(iommufd-bindings-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/iommufd-bindings) = %{version}

%description -n %{name}+iommufd-bindings
This metapackage enables feature "iommufd-bindings" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+iommufd-ioctls
Summary:        Safe wrappers over VFIO ioctls - feature "iommufd-ioctls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(iommufd-ioctls-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/iommufd-ioctls) = %{version}

%description -n %{name}+iommufd-ioctls
This metapackage enables feature "iommufd-ioctls" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kvm
Summary:        Safe wrappers over VFIO ioctls - feature "kvm" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/kvm-bindings) = %{version}
Requires:       crate(%{pkgname}/kvm-ioctls) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/kvm) = %{version}

%description -n %{name}+kvm
This metapackage enables feature "kvm" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+kvm-bindings
Summary:        Safe wrappers over VFIO ioctls - feature "kvm-bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kvm-bindings-0.14/default) >= 0.14.0
Provides:       crate(%{pkgname}/kvm-bindings) = %{version}

%description -n %{name}+kvm-bindings
This metapackage enables feature "kvm-bindings" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+kvm-ioctls
Summary:        Safe wrappers over VFIO ioctls - feature "kvm-ioctls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(kvm-ioctls-0.24/default) >= 0.24.0
Provides:       crate(%{pkgname}/kvm-ioctls) = %{version}

%description -n %{name}+kvm-ioctls
This metapackage enables feature "kvm-ioctls" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mshv
Summary:        Safe wrappers over VFIO ioctls - feature "mshv"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/mshv-bindings) = %{version}
Requires:       crate(%{pkgname}/mshv-ioctls) = %{version}
Provides:       crate(%{pkgname}/mshv) = %{version}

%description -n %{name}+mshv
This metapackage enables feature "mshv" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mshv-bindings
Summary:        Safe wrappers over VFIO ioctls - feature "mshv-bindings"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mshv-bindings-0.6/default) >= 0.6.5
Requires:       crate(mshv-bindings-0.6/fam-wrappers) >= 0.6.5
Requires:       crate(mshv-bindings-0.6/with-serde) >= 0.6.5
Provides:       crate(%{pkgname}/mshv-bindings) = %{version}

%description -n %{name}+mshv-bindings
This metapackage enables feature "mshv-bindings" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+mshv-ioctls
Summary:        Safe wrappers over VFIO ioctls - feature "mshv-ioctls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(mshv-ioctls-0.6/default) >= 0.6.5
Provides:       crate(%{pkgname}/mshv-ioctls) = %{version}

%description -n %{name}+mshv-ioctls
This metapackage enables feature "mshv-ioctls" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vfio-cdev
Summary:        Safe wrappers over VFIO ioctls - feature "vfio_cdev"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/iommufd-bindings) = %{version}
Requires:       crate(%{pkgname}/iommufd-ioctls) = %{version}
Requires:       crate(%{pkgname}/kvm) = %{version}
Provides:       crate(%{pkgname}/vfio-cdev) = %{version}

%description -n %{name}+vfio-cdev
This metapackage enables feature "vfio_cdev" for the Rust vfio-ioctls crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

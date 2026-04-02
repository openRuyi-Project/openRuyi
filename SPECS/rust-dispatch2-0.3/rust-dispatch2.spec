# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name dispatch2
%global full_version 0.3.1
%global pkgname dispatch2-0.3

Name:           rust-dispatch2-0.3
Version:        0.3.1
Release:        %autorelease
Summary:        Rust crate "dispatch2"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:1e0e367e4e7da84520dedcac1901e4da967309406d1e51017ae1abfb97adbd38
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(bitflags-2.0/std) >= 2.11.0
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/std)

%description
Source code for takopackized Rust crate "dispatch2"

%package     -n %{name}+block2
Summary:        Bindings and wrappers for Apple's Grand Central Dispatch (GCD) - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust dispatch2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings and wrappers for Apple's Grand Central Dispatch (GCD) - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/libc)
Requires:       crate(%{pkgname}/objc2)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust dispatch2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+libc
Summary:        Bindings and wrappers for Apple's Grand Central Dispatch (GCD) - feature "libc"
Requires:       crate(%{pkgname})
Requires:       crate(libc-0.2) >= 0.2.80
Provides:       crate(%{pkgname}/libc)

%description -n %{name}+libc
This metapackage enables feature "libc" for the Rust dispatch2 crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2
Summary:        Bindings and wrappers for Apple's Grand Central Dispatch (GCD) - feature "objc2"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-0.6/std) >= 0.6.4
Provides:       crate(%{pkgname}/objc2)

%description -n %{name}+objc2
This metapackage enables feature "objc2" for the Rust dispatch2 crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

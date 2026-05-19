# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name ring
%global full_version 0.16.20
%global pkgname ring-0.16

Name:           rust-ring-0.16
Version:        0.16.20
Release:        %autorelease
Summary:        Rust crate "ring"
License:        FIXME
URL:            https://github.com/briansmith/ring
#!RemoteAsset:  sha256:3053cf52e236a3ed746dfc745aa9cacf1b791d846bdaf412f60a8d7d6e17c8fc
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cc-1.0) >= 1.0.62
Requires:       crate(libc-0.2) >= 0.2.69
Requires:       crate(once-cell-1.0/std) >= 1.5.2
Requires:       crate(spin-0.5) >= 0.5.2
Requires:       crate(untrusted-0.7/default) >= 0.7.1
Requires:       crate(web-sys-0.3/crypto) >= 0.3.37
Requires:       crate(web-sys-0.3/window) >= 0.3.37
Requires:       crate(winapi-0.3/ntsecapi) >= 0.3.8
Requires:       crate(winapi-0.3/wtypesbase) >= 0.3.8
Provides:       crate(ring) = %{version}
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/internal-benches)
Provides:       crate(%{pkgname}/slow-tests)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/test-logging)
Provides:       crate(%{pkgname}/wasm32-c)

%description
Source code for takopackized Rust crate "ring"

%package     -n %{name}+default
Summary:        Safe, fast, small crypto using Rust - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/alloc)
Requires:       crate(%{pkgname}/dev-urandom-fallback)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Safe, fast, small crypto using Rust - feature "once_cell" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(once-cell-1.0/std) >= 1.5.2
Provides:       crate(%{pkgname}/dev-urandom-fallback)
Provides:       crate(%{pkgname}/once-cell)

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust ring crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "dev_urandom_fallback" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

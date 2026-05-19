# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mimalloc
%global full_version 0.1.50
%global pkgname mimalloc-0.1

Name:           rust-mimalloc-0.1
Version:        0.1.50
Release:        %autorelease
Summary:        Rust crate "mimalloc"
License:        MIT
URL:            https://github.com/purpleprotocol/mimalloc_rust
#!RemoteAsset:  sha256:b3627c4272df786b9260cabaa46aec1d59c93ede723d4c3ef646c503816b0640
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libmimalloc-sys-0.1) >= 0.1.47
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/default)

%description
Source code for takopackized Rust crate "mimalloc"

%package     -n %{name}+debug
Summary:        Performance and security oriented drop-in allocator - feature "debug"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/debug) >= 0.1.47
Provides:       crate(%{pkgname}/debug)

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug-in-debug
Summary:        Performance and security oriented drop-in allocator - feature "debug_in_debug"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/debug-in-debug) >= 0.1.47
Provides:       crate(%{pkgname}/debug-in-debug)

%description -n %{name}+debug-in-debug
This metapackage enables feature "debug_in_debug" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extended
Summary:        Performance and security oriented drop-in allocator - feature "extended"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/extended) >= 0.1.47
Provides:       crate(%{pkgname}/extended)

%description -n %{name}+extended
This metapackage enables feature "extended" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+local-dynamic-tls
Summary:        Performance and security oriented drop-in allocator - feature "local_dynamic_tls"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/local-dynamic-tls) >= 0.1.47
Provides:       crate(%{pkgname}/local-dynamic-tls)

%description -n %{name}+local-dynamic-tls
This metapackage enables feature "local_dynamic_tls" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-thp
Summary:        Performance and security oriented drop-in allocator - feature "no_thp"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/no-thp) >= 0.1.47
Provides:       crate(%{pkgname}/no-thp)

%description -n %{name}+no-thp
This metapackage enables feature "no_thp" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+override
Summary:        Performance and security oriented drop-in allocator - feature "override"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/override) >= 0.1.47
Provides:       crate(%{pkgname}/override)

%description -n %{name}+override
This metapackage enables feature "override" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+secure
Summary:        Performance and security oriented drop-in allocator - feature "secure"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/secure) >= 0.1.47
Provides:       crate(%{pkgname}/secure)

%description -n %{name}+secure
This metapackage enables feature "secure" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2
Summary:        Performance and security oriented drop-in allocator - feature "v2"
Requires:       crate(%{pkgname})
Requires:       crate(libmimalloc-sys-0.1/v2) >= 0.1.47
Provides:       crate(%{pkgname}/v2)

%description -n %{name}+v2
This metapackage enables feature "v2" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

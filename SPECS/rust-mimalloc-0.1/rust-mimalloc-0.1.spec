# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name mimalloc
%global full_version 0.1.52
%global pkgname mimalloc-0.1

Name:           rust-mimalloc-0.1
Version:        0.1.52
Release:        %autorelease
Summary:        Rust crate "mimalloc"
License:        MIT
URL:            https://github.com/purpleprotocol/mimalloc_rust
#!RemoteAsset:  sha256:2d4139bb28d14ad1facf21d5eb8825051b326e172d216b39f6d31df53cc97862
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(libmimalloc-sys-0.1) >= 0.1.49
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "mimalloc"

%package     -n %{name}+debug
Summary:        Performance and security oriented drop-in allocator - feature "debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/debug) >= 0.1.49
Provides:       crate(%{pkgname}/debug) = %{version}

%description -n %{name}+debug
This metapackage enables feature "debug" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+debug-in-debug
Summary:        Performance and security oriented drop-in allocator - feature "debug_in_debug"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/debug-in-debug) >= 0.1.49
Provides:       crate(%{pkgname}/debug-in-debug) = %{version}

%description -n %{name}+debug-in-debug
This metapackage enables feature "debug_in_debug" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+extended
Summary:        Performance and security oriented drop-in allocator - feature "extended"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/extended) >= 0.1.49
Provides:       crate(%{pkgname}/extended) = %{version}

%description -n %{name}+extended
This metapackage enables feature "extended" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+local-dynamic-tls
Summary:        Performance and security oriented drop-in allocator - feature "local_dynamic_tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/local-dynamic-tls) >= 0.1.49
Provides:       crate(%{pkgname}/local-dynamic-tls) = %{version}

%description -n %{name}+local-dynamic-tls
This metapackage enables feature "local_dynamic_tls" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+no-thp
Summary:        Performance and security oriented drop-in allocator - feature "no_thp"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/no-thp) >= 0.1.49
Provides:       crate(%{pkgname}/no-thp) = %{version}

%description -n %{name}+no-thp
This metapackage enables feature "no_thp" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+override
Summary:        Performance and security oriented drop-in allocator - feature "override"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/override) >= 0.1.49
Provides:       crate(%{pkgname}/override) = %{version}

%description -n %{name}+override
This metapackage enables feature "override" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+secure
Summary:        Performance and security oriented drop-in allocator - feature "secure"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/secure) >= 0.1.49
Provides:       crate(%{pkgname}/secure) = %{version}

%description -n %{name}+secure
This metapackage enables feature "secure" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+v2
Summary:        Performance and security oriented drop-in allocator - feature "v2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/v2) >= 0.1.49
Provides:       crate(%{pkgname}/v2) = %{version}

%description -n %{name}+v2
This metapackage enables feature "v2" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+win-direct-tls
Summary:        Performance and security oriented drop-in allocator - feature "win_direct_tls"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(libmimalloc-sys-0.1/win-direct-tls) >= 0.1.49
Provides:       crate(%{pkgname}/win-direct-tls) = %{version}

%description -n %{name}+win-direct-tls
This metapackage enables feature "win_direct_tls" for the Rust mimalloc crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

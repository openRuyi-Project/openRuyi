# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name inferno
%global full_version 0.11.21
%global pkgname inferno-0.11

Name:           rust-inferno-0.11
Version:        0.11.21
Release:        %autorelease
Summary:        Rust crate "inferno"
License:        CDDL-1.0
URL:            https://github.com/jonhoo/inferno.git
#!RemoteAsset:  sha256:232929e1d75fe899576a3d5c7416ad0d88dbfbb3c3d6aa00873a7408a50ddb88
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(ahash-0.8/default) >= 0.8.0
Requires:       crate(is-terminal-0.4/default) >= 0.4.3
Requires:       crate(itoa-1/default) >= 1.0.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(num-format-0.4) >= 0.4.3
Requires:       crate(once-cell-1/default) >= 1.12.0
Requires:       crate(quick-xml-0.26) >= 0.26.0
Requires:       crate(rgb-0.8/default) >= 0.8.13
Requires:       crate(str-stack-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "inferno"

%package     -n %{name}+clap
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.0.1
Requires:       crate(clap-4/derive) >= 4.0.1
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+cli
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "cli"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/clap) = %{version}
Requires:       crate(%{pkgname}/env-logger) = %{version}
Provides:       crate(%{pkgname}/cli) = %{version}

%description -n %{name}+cli
This metapackage enables feature "cli" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-channel
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "crossbeam-channel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-channel-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/crossbeam-channel) = %{version}

%description -n %{name}+crossbeam-channel
This metapackage enables feature "crossbeam-channel" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crossbeam-utils
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "crossbeam-utils"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(crossbeam-utils-0.8/default) >= 0.8.0
Provides:       crate(%{pkgname}/crossbeam-utils) = %{version}

%description -n %{name}+crossbeam-utils
This metapackage enables feature "crossbeam-utils" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+dashmap
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "dashmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(dashmap-6/default) >= 6.0.1
Provides:       crate(%{pkgname}/dashmap) = %{version}

%description -n %{name}+dashmap
This metapackage enables feature "dashmap" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/cli) = %{version}
Requires:       crate(%{pkgname}/multithreaded) = %{version}
Requires:       crate(%{pkgname}/nameattr) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+env-logger
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "env_logger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(env-logger-0.11) >= 0.11.0
Provides:       crate(%{pkgname}/env-logger) = %{version}

%description -n %{name}+env-logger
This metapackage enables feature "env_logger" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+indexmap
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "indexmap" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(indexmap-2/default) >= 2.0.0
Provides:       crate(%{pkgname}/indexmap) = %{version}
Provides:       crate(%{pkgname}/nameattr) = %{version}

%description -n %{name}+indexmap
This metapackage enables feature "indexmap" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "nameattr" feature.

%package     -n %{name}+multithreaded
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "multithreaded"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crossbeam-channel) = %{version}
Requires:       crate(%{pkgname}/crossbeam-utils) = %{version}
Requires:       crate(%{pkgname}/dashmap) = %{version}
Provides:       crate(%{pkgname}/multithreaded) = %{version}

%description -n %{name}+multithreaded
This metapackage enables feature "multithreaded" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+regex
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1) >= 1.6.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+rle-decode-fast
Summary:        Rust port of the FlameGraph performance profiling tool suite - feature "rle-decode-fast"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(rle-decode-fast-1) >= 1.0.3
Provides:       crate(%{pkgname}/rle-decode-fast) = %{version}

%description -n %{name}+rle-decode-fast
This metapackage enables feature "rle-decode-fast" for the Rust inferno crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name interprocess
%global full_version 1.2.1
%global pkgname interprocess-1

Name:           rust-interprocess-1
Version:        1.2.1
Release:        %autorelease
Summary:        Rust crate "interprocess"
License:        MIT OR Apache-2.0
URL:            https://github.com/kotauskas/interprocess
#!RemoteAsset:  sha256:81f2533f3be42fffe3b5e63b71aeca416c1c3bc33e4e27be018521e76b1f38fb
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(cfg-if-1/default) >= 1.0.0
Requires:       crate(libc-0.2/default) >= 0.2.137
Requires:       crate(libc-0.2/extra-traits) >= 0.2.137
Requires:       crate(rustc-version-0.4) >= 0.4.0
Requires:       crate(to-method-1/default) >= 1.1.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/fileapi) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/namedpipeapi) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0
Requires:       crate(winapi-0.3/std) >= 0.3.0
Requires:       crate(winapi-0.3/winbase) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/doc-cfg) = %{version}

%description
Source code for takopackized Rust crate "interprocess"

%package     -n %{name}+blocking
Summary:        Interprocess communication toolkit - feature "blocking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(blocking-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/blocking) = %{version}

%description -n %{name}+blocking
This metapackage enables feature "blocking" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Interprocess communication toolkit - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/nonblocking) = %{version}
Requires:       crate(%{pkgname}/signals) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core
Summary:        Interprocess communication toolkit - feature "futures-core"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-core) = %{version}

%description -n %{name}+futures-core
This metapackage enables feature "futures-core" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io
Summary:        Interprocess communication toolkit - feature "futures-io"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/futures-io) = %{version}

%description -n %{name}+futures-io
This metapackage enables feature "futures-io" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+intmap
Summary:        Interprocess communication toolkit - feature "intmap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(intmap-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/intmap) = %{version}

%description -n %{name}+intmap
This metapackage enables feature "intmap" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nonblocking
Summary:        Interprocess communication toolkit - feature "nonblocking"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/blocking) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Provides:       crate(%{pkgname}/nonblocking) = %{version}

%description -n %{name}+nonblocking
This metapackage enables feature "nonblocking" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Interprocess communication toolkit - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.7.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+signals
Summary:        Interprocess communication toolkit - feature "signals"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/intmap) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Requires:       crate(%{pkgname}/spinning) = %{version}
Requires:       crate(%{pkgname}/thiserror) = %{version}
Provides:       crate(%{pkgname}/signals) = %{version}

%description -n %{name}+signals
This metapackage enables feature "signals" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+spinning
Summary:        Interprocess communication toolkit - feature "spinning"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(spinning-0.1/default) >= 0.1.0
Provides:       crate(%{pkgname}/spinning) = %{version}

%description -n %{name}+spinning
This metapackage enables feature "spinning" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+thiserror
Summary:        Interprocess communication toolkit - feature "thiserror"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(thiserror-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/thiserror) = %{version}

%description -n %{name}+thiserror
This metapackage enables feature "thiserror" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio
Summary:        Interprocess communication toolkit - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/default) >= 1.8.0
Requires:       crate(tokio-1/io-util) >= 1.8.0
Requires:       crate(tokio-1/net) >= 1.8.0
Requires:       crate(tokio-1/time) >= 1.8.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-support
Summary:        Interprocess communication toolkit - feature "tokio_support"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core) = %{version}
Requires:       crate(%{pkgname}/futures-io) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Provides:       crate(%{pkgname}/tokio-support) = %{version}

%description -n %{name}+tokio-support
This metapackage enables feature "tokio_support" for the Rust interprocess crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

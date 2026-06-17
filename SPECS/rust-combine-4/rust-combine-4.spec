# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name combine
%global full_version 4.6.7
%global pkgname combine-4

Name:           rust-combine-4
Version:        4.6.7
Release:        %autorelease
Summary:        Rust crate "combine"
License:        MIT
URL:            https://github.com/Marwes/combine
#!RemoteAsset:  sha256:ba5a308b75df32fe02788e748662718f03fde005016435c444eea572398219fd
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(memchr-2) >= 2.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/alloc) = %{version}
Provides:       crate(%{pkgname}/mp4) = %{version}

%description
Source code for takopackized Rust crate "combine"

%package     -n %{name}+bytes
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes-05
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "bytes_05"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/bytes-05) = %{version}

%description -n %{name}+bytes-05
This metapackage enables feature "bytes_05" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-03
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "futures-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core-03) = %{version}
Requires:       crate(%{pkgname}/futures-io-03) = %{version}
Requires:       crate(%{pkgname}/pin-project) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Provides:       crate(%{pkgname}/futures-03) = %{version}

%description -n %{name}+futures-03
This metapackage enables feature "futures-03" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-core-03
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "futures-core-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-core-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/futures-core-03) = %{version}

%description -n %{name}+futures-core-03
This metapackage enables feature "futures-core-03" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+futures-io-03
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "futures-io-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-io-0.3) >= 0.3.1
Provides:       crate(%{pkgname}/futures-io-03) = %{version}

%description -n %{name}+futures-io-03
This metapackage enables feature "futures-io-03" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pin-project-lite
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "pin-project-lite" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pin-project-lite-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/pin-project) = %{version}
Provides:       crate(%{pkgname}/pin-project-lite) = %{version}

%description -n %{name}+pin-project-lite
This metapackage enables feature "pin-project-lite" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "pin-project" feature.

%package     -n %{name}+regex
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "regex"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(regex-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/regex) = %{version}

%description -n %{name}+regex
This metapackage enables feature "regex" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(memchr-2/std) >= 2.3.0
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+tokio
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core-03) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/tokio-dep) = %{version}
Requires:       crate(tokio-util-0.7/codec) >= 0.7.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-02
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-02"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bytes-05) = %{version}
Requires:       crate(%{pkgname}/futures-core-03) = %{version}
Requires:       crate(%{pkgname}/pin-project) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio-02-dep) = %{version}
Provides:       crate(%{pkgname}/tokio-02) = %{version}

%description -n %{name}+tokio-02
This metapackage enables feature "tokio-02" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-02-dep
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-02-dep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-0.2/io-util) >= 0.2.3
Provides:       crate(%{pkgname}/tokio-02-dep) = %{version}

%description -n %{name}+tokio-02-dep
This metapackage enables feature "tokio-02-dep" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-03
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-03"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/futures-core-03) = %{version}
Requires:       crate(%{pkgname}/pin-project) = %{version}
Requires:       crate(%{pkgname}/pin-project-lite) = %{version}
Requires:       crate(%{pkgname}/std) = %{version}
Requires:       crate(%{pkgname}/tokio-03-dep) = %{version}
Provides:       crate(%{pkgname}/tokio-03) = %{version}

%description -n %{name}+tokio-03
This metapackage enables feature "tokio-03" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-03-dep
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-03-dep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-0.3) >= 0.3.0
Provides:       crate(%{pkgname}/tokio-03-dep) = %{version}

%description -n %{name}+tokio-03-dep
This metapackage enables feature "tokio-03-dep" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-dep
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-dep"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1) >= 1.0.0
Provides:       crate(%{pkgname}/tokio-dep) = %{version}

%description -n %{name}+tokio-dep
This metapackage enables feature "tokio-dep" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        Fast parser combinators on arbitrary streams with zero-copy support - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/codec) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust combine crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

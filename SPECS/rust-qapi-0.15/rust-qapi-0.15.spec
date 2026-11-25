# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name qapi
%global full_version 0.15.0
%global pkgname qapi-0.15

Name:           rust-qapi-0.15
Version:        0.15.0
Release:        %autorelease
Summary:        Rust crate "qapi"
License:        MIT
URL:            https://github.com/arcnmx/qapi-rs
#!RemoteAsset:  sha256:7b047adab56acc4948d4b9b58693c1f33fd13efef2d6bb5f0f66a47436ceada8
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(log-0.4/default) >= 0.4.6
Requires:       crate(qapi-spec-0.3/default) >= 0.3.0
Requires:       crate(serde-1/default) >= 1.0.27
Requires:       crate(serde-json-1/default) >= 1.0.9

Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "qapi"

%package     -n %{name}+async-tokio
Summary:        QEMU QMP and Guest Agent API - feature "async-tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/bytes) = %{version}
Requires:       crate(%{pkgname}/memchr) = %{version}
Requires:       crate(%{pkgname}/tokio) = %{version}
Requires:       crate(%{pkgname}/tokio-util) = %{version}
Provides:       crate(%{pkgname}/async-tokio) = %{version}

%description -n %{name}+async-tokio
This metapackage enables feature "async-tokio" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio-all
Summary:        QEMU QMP and Guest Agent API - feature "async-tokio-all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-tokio-net) = %{version}
Requires:       crate(%{pkgname}/async-tokio-spawn) = %{version}
Provides:       crate(%{pkgname}/async-tokio-all) = %{version}

%description -n %{name}+async-tokio-all
This metapackage enables feature "async-tokio-all" for the Rust qapi crate,
by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio-net
Summary:        QEMU QMP and Guest Agent API - feature "async-tokio-net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-tokio) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/net) >= 1.0.0
Provides:       crate(%{pkgname}/async-tokio-net) = %{version}

%description -n %{name}+async-tokio-net
This metapackage enables feature "async-tokio-net" for the Rust qapi crate,
by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tokio-spawn
Summary:        QEMU QMP and Guest Agent API - feature "async-tokio-spawn"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async-tokio) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Requires:       crate(tokio-1/rt) >= 1.0.0
Provides:       crate(%{pkgname}/async-tokio-spawn) = %{version}

%description -n %{name}+async-tokio-spawn
This metapackage enables feature "async-tokio-spawn" for the Rust qapi
crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+async-tower
Summary:        QEMU QMP and Guest Agent API - feature "async-tower"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/tower-service) = %{version}
Provides:       crate(%{pkgname}/async-tower) = %{version}

%description -n %{name}+async-tower
This metapackage enables feature "async-tower" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bytes
Summary:        QEMU QMP and Guest Agent API - feature "bytes"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bytes-1/default) >= 1.0.0
Provides:       crate(%{pkgname}/bytes) = %{version}

%description -n %{name}+bytes
This metapackage enables feature "bytes" for the Rust qapi crate, by pulling
in any additional dependencies needed by that feature.

%package     -n %{name}+futures
Summary:        QEMU QMP and Guest Agent API - feature "futures" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-0.3/default) >= 0.3.5
Provides:       crate(%{pkgname}/async) = %{version}
Provides:       crate(%{pkgname}/futures) = %{version}

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "async" feature.

%package     -n %{name}+memchr
Summary:        QEMU QMP and Guest Agent API - feature "memchr"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(memchr-2/default) >= 2.3.3
Provides:       crate(%{pkgname}/memchr) = %{version}

%description -n %{name}+memchr
This metapackage enables feature "memchr" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+qapi-qga
Summary:        QEMU QMP and Guest Agent API - feature "qapi-qga" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(qapi-qga-0.13/default) >= 0.13.0
Provides:       crate(%{pkgname}/qapi-qga) = %{version}
Provides:       crate(%{pkgname}/qga) = %{version}

%description -n %{name}+qapi-qga
This metapackage enables feature "qapi-qga" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "qga" feature.

%package     -n %{name}+qapi-qmp
Summary:        QEMU QMP and Guest Agent API - feature "qapi-qmp" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(qapi-qmp-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/qapi-qmp) = %{version}
Provides:       crate(%{pkgname}/qmp) = %{version}

%description -n %{name}+qapi-qmp
This metapackage enables feature "qapi-qmp" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "qmp" feature.

%package     -n %{name}+tokio
Summary:        QEMU QMP and Guest Agent API - feature "tokio"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-1/io-util) >= 1.0.0
Provides:       crate(%{pkgname}/tokio) = %{version}

%description -n %{name}+tokio
This metapackage enables feature "tokio" for the Rust qapi crate, by pulling
in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-util
Summary:        QEMU QMP and Guest Agent API - feature "tokio-util"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tokio-util-0.7/codec) >= 0.7.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Provides:       crate(%{pkgname}/tokio-util) = %{version}

%description -n %{name}+tokio-util
This metapackage enables feature "tokio-util" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tower-service
Summary:        QEMU QMP and Guest Agent API - feature "tower-service"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(tower-service-0.3/default) >= 0.3.0
Provides:       crate(%{pkgname}/tower-service) = %{version}

%description -n %{name}+tower-service
This metapackage enables feature "tower-service" for the Rust qapi crate, by
pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

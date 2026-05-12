# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serial_test
%global full_version 2.0.0
%global pkgname serial-test-2.0

Name:           rust-serial-test-2.0
Version:        2.0.0
Release:        %autorelease
Summary:        Rust crate "serial_test"
License:        MIT
URL:            https://github.com/palfrey/serial_test/
#!RemoteAsset:  sha256:0e56dd856803e253c8f298af3f4d7eb0ae5e23a737252cd90bb4f3b435033b2d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(dashmap-5.0/default) >= 5.5.3
Requires:       crate(lazy-static-1.0/default) >= 1.5.0
Requires:       crate(parking-lot-0.12/default) >= 0.12.5
Requires:       crate(serial-test-derive-2.0/default) >= 2.0.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "serial_test"

%package     -n %{name}+async
Summary:        Allows for the creation of serialised Rust tests - feature "async"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/futures)
Requires:       crate(serial-test-derive-2.0/async) >= 2.0.0
Provides:       crate(%{pkgname}/async)

%description -n %{name}+async
This metapackage enables feature "async" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Allows for the creation of serialised Rust tests - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/async)
Requires:       crate(%{pkgname}/logging)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+document-features
Summary:        Allows for the creation of serialised Rust tests - feature "document-features" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/docsrs)
Provides:       crate(%{pkgname}/document-features)

%description -n %{name}+document-features
This metapackage enables feature "document-features" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "docsrs" feature.

%package     -n %{name}+fslock
Summary:        Allows for the creation of serialised Rust tests - feature "fslock" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(fslock-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/file-locks)
Provides:       crate(%{pkgname}/fslock)

%description -n %{name}+fslock
This metapackage enables feature "fslock" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "file_locks" feature.

%package     -n %{name}+futures
Summary:        Allows for the creation of serialised Rust tests - feature "futures"
Requires:       crate(%{pkgname})
Requires:       crate(futures-0.3/executor) >= 0.3.0
Provides:       crate(%{pkgname}/futures)

%description -n %{name}+futures
This metapackage enables feature "futures" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+log
Summary:        Allows for the creation of serialised Rust tests - feature "log" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(log-0.4/default) >= 0.4.0
Provides:       crate(%{pkgname}/log)
Provides:       crate(%{pkgname}/logging)

%description -n %{name}+log
This metapackage enables feature "log" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "logging" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

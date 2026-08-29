# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name serial_test
%global full_version 3.5.0
%global pkgname serial-test-3

Name:           rust-serial-test-3
Version:        3.5.0
Release:        %autorelease
Summary:        Rust crate "serial_test"
License:        MIT
URL:            https://github.com/palfrey/serial_test/
#!RemoteAsset:  sha256:699f4197115b8a7e7ff19c9a315a4bd6fffec26cc4626ef45ecaea389e081c6d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(once-cell-1/std) >= 1.19.0
Requires:       crate(parking-lot-0.12) >= 0.12.0
Requires:       crate(serial-test-derive-3/default) >= 3.5.0
Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "serial_test"

%package     -n %{name}+async
Summary:        Allows for the creation of serialised Rust tests - feature "async"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(futures-executor-0.3/std) >= 0.3.0
Requires:       crate(futures-util-0.3/std) >= 0.3.0
Requires:       crate(serial-test-derive-3/async) >= 3.5.0
Provides:       crate(%{pkgname}/async) = %{version}

%description -n %{name}+async
This metapackage enables feature "async" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Allows for the creation of serialised Rust tests - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/async) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+docsrs
Summary:        Allows for the creation of serialised Rust tests - feature "docsrs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(document-features-0.2/default) >= 0.2.0
Provides:       crate(%{pkgname}/docsrs) = %{version}

%description -n %{name}+docsrs
This metapackage enables feature "docsrs" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+file-locks
Summary:        Allows for the creation of serialised Rust tests - feature "file_locks"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(fslock-0.2/std) >= 0.2.0
Provides:       crate(%{pkgname}/file-locks) = %{version}

%description -n %{name}+file-locks
This metapackage enables feature "file_locks" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+logging
Summary:        Allows for the creation of serialised Rust tests - feature "logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(log-0.4/default) >= 0.4.4
Provides:       crate(%{pkgname}/logging) = %{version}

%description -n %{name}+logging
This metapackage enables feature "logging" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+test-logging
Summary:        Allows for the creation of serialised Rust tests - feature "test_logging"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/logging) = %{version}
Requires:       crate(env-logger-0.6) >= 0.6.1
Requires:       crate(serial-test-derive-3/test-logging) >= 3.5.0
Provides:       crate(%{pkgname}/test-logging) = %{version}

%description -n %{name}+test-logging
This metapackage enables feature "test_logging" for the Rust serial_test crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

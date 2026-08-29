# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rustls-platform-verifier
%global full_version 0.6.2
%global pkgname rustls-platform-verifier-0.6

Name:           rust-rustls-platform-verifier-0.6
Version:        0.6.2
Release:        %autorelease
Summary:        Rust crate "rustls-platform-verifier"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/rustls-platform-verifier
#!RemoteAsset:  sha256:1d99feebc72bae7ab76ba994bb5e121b8d83d910ca40b36e0921f53becc41784
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(core-foundation-0.10/default) >= 0.10.0
Requires:       crate(core-foundation-sys-0.8/default) >= 0.8.0
Requires:       crate(jni-0.21) >= 0.21.0
Requires:       crate(log-0.4/default) >= 0.4.0
Requires:       crate(once-cell-1/default) >= 1.9.0
Requires:       crate(rustls-0.23/std) >= 0.23.27
Requires:       crate(rustls-native-certs-0.8/default) >= 0.8.0
Requires:       crate(rustls-platform-verifier-android-0.1/default) >= 0.1.0
Requires:       crate(rustls-webpki-0.103) >= 0.103.0
Requires:       crate(security-framework-3/default) >= 3.5.0
Requires:       crate(security-framework-sys-2/default) >= 2.15.0
Requires:       crate(webpki-root-certs-1/default) >= 1.0.0
Requires:       crate(windows-sys-0.52/win32-foundation) >= 0.52.0
Requires:       crate(windows-sys-0.52/win32-security-cryptography) >= 0.52.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/dbg) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description
Source code for takopackized Rust crate "rustls-platform-verifier"

%package     -n %{name}+android-logger
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "android_logger"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(android-logger-0.15/default) >= 0.15.0
Provides:       crate(%{pkgname}/android-logger) = %{version}

%description -n %{name}+android-logger
This metapackage enables feature "android_logger" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+base64
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "base64" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(base64-0.22/default) >= 0.22.0
Provides:       crate(%{pkgname}/base64) = %{version}
Provides:       crate(%{pkgname}/cert-logging) = %{version}

%description -n %{name}+base64
This metapackage enables feature "base64" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "cert-logging" feature.

%package     -n %{name}+docsrs
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "docsrs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/jni) = %{version}
Requires:       crate(%{pkgname}/once-cell) = %{version}
Provides:       crate(%{pkgname}/docsrs) = %{version}

%description -n %{name}+docsrs
This metapackage enables feature "docsrs" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ffi-testing
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "ffi-testing"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/android-logger) = %{version}
Requires:       crate(rustls-0.23/ring) >= 0.23.27
Requires:       crate(rustls-0.23/std) >= 0.23.27
Provides:       crate(%{pkgname}/ffi-testing) = %{version}

%description -n %{name}+ffi-testing
This metapackage enables feature "ffi-testing" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+jni
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "jni"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(jni-0.21) >= 0.21.0
Provides:       crate(%{pkgname}/jni) = %{version}

%description -n %{name}+jni
This metapackage enables feature "jni" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+once-cell
Summary:        Rustls-platform-verifier supports verifying TLS certificates in rustls with the operating system verifier - feature "once_cell"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(once-cell-1/default) >= 1.9.0
Provides:       crate(%{pkgname}/once-cell) = %{version}

%description -n %{name}+once-cell
This metapackage enables feature "once_cell" for the Rust rustls-platform-verifier crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

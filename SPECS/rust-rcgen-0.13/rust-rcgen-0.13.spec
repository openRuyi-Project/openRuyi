# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name rcgen
%global full_version 0.13.2
%global pkgname rcgen-0.13

Name:           rust-rcgen-0.13
Version:        0.13.2
Release:        %autorelease
Summary:        Rust crate "rcgen"
License:        MIT OR Apache-2.0
URL:            https://github.com/rustls/rcgen
#!RemoteAsset:  sha256:75e669e5202259b5314d1ea5397316ad400819437857b90861765f24c4cf80a2
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(rustls-pki-types-1/default) >= 1.4.1
Requires:       crate(time-0.3) >= 0.3.6
Requires:       crate(yasna-0.5/default) >= 0.5.2
Requires:       crate(yasna-0.5/std) >= 0.5.2
Requires:       crate(yasna-0.5/time) >= 0.5.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/crypto) = %{version}

%description
Source code for takopackized Rust crate "rcgen"

%package     -n %{name}+aws-lc-rs
Summary:        Rust X.509 certificate generator - feature "aws_lc_rs"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crypto) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.6.0
Requires:       crate(aws-lc-rs-1/aws-lc-sys) >= 1.6.0
Provides:       crate(%{pkgname}/aws-lc-rs) = %{version}

%description -n %{name}+aws-lc-rs
This metapackage enables feature "aws_lc_rs" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Rust X.509 certificate generator - feature "default"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crypto) = %{version}
Requires:       crate(%{pkgname}/pem) = %{version}
Requires:       crate(%{pkgname}/ring) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+default
This metapackage enables feature "default" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+fips
Summary:        Rust X.509 certificate generator - feature "fips"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crypto) = %{version}
Requires:       crate(aws-lc-rs-1) >= 1.6.0
Requires:       crate(aws-lc-rs-1/fips) >= 1.6.0
Provides:       crate(%{pkgname}/fips) = %{version}

%description -n %{name}+fips
This metapackage enables feature "fips" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+pem
Summary:        Rust X.509 certificate generator - feature "pem"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pem-3/default) >= 3.0.2
Provides:       crate(%{pkgname}/pem) = %{version}

%description -n %{name}+pem
This metapackage enables feature "pem" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+ring
Summary:        Rust X.509 certificate generator - feature "ring"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/crypto) = %{version}
Requires:       crate(ring-0.17/default) >= 0.17.0
Provides:       crate(%{pkgname}/ring) = %{version}

%description -n %{name}+ring
This metapackage enables feature "ring" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+x509-parser
Summary:        Rust X.509 certificate generator - feature "x509-parser"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(x509-parser-0.16/default) >= 0.16.0
Requires:       crate(x509-parser-0.16/verify) >= 0.16.0
Provides:       crate(%{pkgname}/x509-parser) = %{version}

%description -n %{name}+x509-parser
This metapackage enables feature "x509-parser" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+zeroize
Summary:        Rust X.509 certificate generator - feature "zeroize"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(zeroize-1/default) >= 1.2.0
Provides:       crate(%{pkgname}/zeroize) = %{version}

%description -n %{name}+zeroize
This metapackage enables feature "zeroize" for the Rust rcgen crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

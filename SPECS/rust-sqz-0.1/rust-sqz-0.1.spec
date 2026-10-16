# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name sqz
%global full_version 0.1.0
%global pkgname sqz-0.1

Name:           rust-sqz-0.1
Version:        0.1.0
Release:        %autorelease
Summary:        Rust crate "sqz"
License:        LGPL-2.0-or-later
URL:            https://sequoia-pgp.org/
#!RemoteAsset:  sha256:d58214ede6d27f5eb51d0f0ef229491c54e81e0e1bc6e2acd898ef97ac4a3ede
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(aho-corasick-1/default) >= 1.0.0
Requires:       crate(anyhow-1/default) >= 1.0.18
Requires:       crate(chrono-0.4/default) >= 0.4.38
Requires:       crate(crossbeam-0.8/default) >= 0.8.1
Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(filetime-0.2/default) >= 0.2.0
Requires:       crate(fs-extra-1/default) >= 1.0.0
Requires:       crate(gethostname-0.4/default) >= 0.4.0
Requires:       crate(humantime-2/default) >= 2.0.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(once-cell-1/default) >= 1.17.0
Requires:       crate(regex-1/default) >= 1.0.0
Requires:       crate(rusqlite-0.31/default) >= 0.31.0
Requires:       crate(sequoia-autocrypt-0.26) >= 0.26.0
Requires:       crate(sequoia-cert-store-0.7) >= 0.7.6
Requires:       crate(sequoia-directories-0.1/default) >= 0.1.0
Requires:       crate(sequoia-ipc-0.36) >= 0.36.0
Requires:       crate(sequoia-keystore-0.7/default) >= 0.7.0
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-policy-config-0.8/default) >= 0.8.0
Requires:       crate(sequoia-wot-0.15) >= 0.15.3
Requires:       crate(tempfile-3/default) >= 3.1.0
Requires:       crate(terminal-size-0.2/default) >= 0.2.6
Requires:       crate(textwrap-0.15/smawk) >= 0.15.0
Requires:       crate(textwrap-0.15/unicode-width) >= 0.15.0
Requires:       crate(thiserror-1/default) >= 1.0.0
Requires:       crate(toml-edit-0.22/display) >= 0.22.0
Requires:       crate(toml-edit-0.22/parse) >= 0.22.0
Requires:       crate(url-2/default) >= 2.1.0

Provides:       crate(%{pkgname}) = %{version}

%description
Source code for takopackized Rust crate "sqz"

%package     -n %{name}+allow-experimental-crypto
Summary:        High-Level library for Sequoia PGP - feature "allow-experimental-crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/allow-experimental-crypto) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Provides:       crate(%{pkgname}/allow-experimental-crypto) = %{version}

%description -n %{name}+allow-experimental-crypto
This metapackage enables feature "allow-experimental-crypto" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+allow-variable-time-crypto
Summary:        High-Level library for Sequoia PGP - feature "allow-variable-time-crypto"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/allow-variable-time-crypto) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Provides:       crate(%{pkgname}/allow-variable-time-crypto) = %{version}

%description -n %{name}+allow-variable-time-crypto
This metapackage enables feature "allow-variable-time-crypto" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+clap
Summary:        High-Level library for Sequoia PGP - feature "clap"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(clap-4/default) >= 4.5.0
Requires:       crate(clap-4/derive) >= 4.5.0
Requires:       crate(clap-4/string) >= 4.5.0
Provides:       crate(%{pkgname}/clap) = %{version}

%description -n %{name}+clap
This metapackage enables feature "clap" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-botan
Summary:        High-Level library for Sequoia PGP - feature "crypto-botan"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-botan) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-botan) = %{version}

%description -n %{name}+crypto-botan
This metapackage enables feature "crypto-botan" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-botan2
Summary:        High-Level library for Sequoia PGP - feature "crypto-botan2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-botan2) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-botan2) = %{version}

%description -n %{name}+crypto-botan2
This metapackage enables feature "crypto-botan2" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-cng
Summary:        High-Level library for Sequoia PGP - feature "crypto-cng"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-cng) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-cng) = %{version}

%description -n %{name}+crypto-cng
This metapackage enables feature "crypto-cng" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-nettle
Summary:        High-Level library for Sequoia PGP - feature "crypto-nettle" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-nettle) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-nettle) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}

%description -n %{name}+crypto-nettle
This metapackage enables feature "crypto-nettle" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+crypto-openssl
Summary:        High-Level library for Sequoia PGP - feature "crypto-openssl"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-openssl) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-openssl) = %{version}

%description -n %{name}+crypto-openssl
This metapackage enables feature "crypto-openssl" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+crypto-rust
Summary:        High-Level library for Sequoia PGP - feature "crypto-rust"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-openpgp-2/compression) >= 2.4.0
Requires:       crate(sequoia-openpgp-2/crypto-rust) >= 2.4.0
Provides:       crate(%{pkgname}/crypto-rust) = %{version}

%description -n %{name}+crypto-rust
This metapackage enables feature "crypto-rust" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+net
Summary:        High-Level library for Sequoia PGP - feature "net"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(sequoia-net-0.30) >= 0.30.0
Requires:       crate(tokio-1/default) >= 1.13.1
Provides:       crate(%{pkgname}/net) = %{version}

%description -n %{name}+net
This metapackage enables feature "net" for the Rust sqz crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

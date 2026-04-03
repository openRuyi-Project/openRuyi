# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name cargo
%global full_version 0.91.0
%global pkgname cargo-0.91

Name:           rust-cargo-0.91
Version:        0.91.0
Release:        %autorelease
Summary:        Rust crate "cargo"
License:        MIT OR Apache-2.0
URL:            https://doc.rust-lang.org/cargo/index.html
#!RemoteAsset:  sha256:0f46c7f53180bf46c220e2af1ceff951e2ce088184fa9009ad6915efee25915d
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(annotate-snippets-0.11/default) >= 0.11.5
Requires:       crate(anstream-0.6/default) >= 0.6.19
Requires:       crate(anstyle-1.0/default) >= 1.0.11
Requires:       crate(anyhow-1.0/default) >= 1.0.98
Requires:       crate(base64-0.22/default) >= 0.22.1
Requires:       crate(blake3-1.0/default) >= 1.8.2
Requires:       crate(cargo-credential-0.4/default) >= 0.4.2
Requires:       crate(cargo-credential-libsecret-0.5/default) >= 0.5.0
Requires:       crate(cargo-credential-macos-keychain-0.4/default) >= 0.4.15
Requires:       crate(cargo-credential-wincred-0.4/default) >= 0.4.15
Requires:       crate(cargo-platform-0.3/default) >= 0.3.0
Requires:       crate(cargo-util-0.2/default) >= 0.2.22
Requires:       crate(cargo-util-schemas-0.10/default) >= 0.10.0
Requires:       crate(clap-4.0/default) >= 4.5.40
Requires:       crate(clap-4.0/wrap-help) >= 4.5.40
Requires:       crate(clap-complete-4.0/default) >= 4.5.54
Requires:       crate(clap-complete-4.0/unstable-dynamic) >= 4.5.54
Requires:       crate(color-print-0.3/default) >= 0.3.7
Requires:       crate(crates-io-0.40/default) >= 0.40.12
Requires:       crate(curl-0.4/default) >= 0.4.48
Requires:       crate(curl-0.4/http2) >= 0.4.48
Requires:       crate(curl-sys-0.4/default) >= 0.4.82
Requires:       crate(filetime-0.2/default) >= 0.2.25
Requires:       crate(flate2-1.0/zlib-rs) >= 1.1.2
Requires:       crate(git2-0.20/default) >= 0.20.2
Requires:       crate(git2-curl-0.21/default) >= 0.21.0
Requires:       crate(gix-0.73/dirwalk) >= 0.73.0
Requires:       crate(gix-0.73/parallel) >= 0.73.0
Requires:       crate(gix-0.73/progress-tree) >= 0.73.0
Requires:       crate(gix-0.73/status) >= 0.73.0
Requires:       crate(glob-0.3/default) >= 0.3.2
Requires:       crate(hex-0.4/default) >= 0.4.3
Requires:       crate(hmac-0.12/default) >= 0.12.1
Requires:       crate(home-0.5/default) >= 0.5.11
Requires:       crate(http-auth-0.1) >= 0.1.10
Requires:       crate(ignore-0.4/default) >= 0.4.23
Requires:       crate(im-rc-15.0/default) >= 15.1.0
Requires:       crate(indexmap-2.0/default) >= 2.10.0
Requires:       crate(itertools-0.14/default) >= 0.14.0
Requires:       crate(jiff-0.2/std) >= 0.2.15
Requires:       crate(jobserver-0.1/default) >= 0.1.33
Requires:       crate(lazycell-1.0/default) >= 1.3.0
Requires:       crate(libc-0.2/default) >= 0.2.174
Requires:       crate(libgit2-sys-0.18/default) >= 0.18.2
Requires:       crate(memchr-2.0/default) >= 2.7.5
Requires:       crate(opener-0.8/default) >= 0.8.2
Requires:       crate(os-info-3.0) >= 3.12.0
Requires:       crate(pasetors-0.7/default) >= 0.7.6
Requires:       crate(pasetors-0.7/paserk) >= 0.7.6
Requires:       crate(pasetors-0.7/serde) >= 0.7.6
Requires:       crate(pasetors-0.7/std) >= 0.7.6
Requires:       crate(pasetors-0.7/v3) >= 0.7.6
Requires:       crate(pathdiff-0.2/default) >= 0.2.3
Requires:       crate(rand-0.9/default) >= 0.9.1
Requires:       crate(regex-1.0/default) >= 1.11.1
Requires:       crate(rusqlite-0.36/bundled) >= 0.36.0
Requires:       crate(rusqlite-0.36/default) >= 0.36.0
Requires:       crate(rustc-hash-2.0/default) >= 2.1.1
Requires:       crate(rustc-stable-hash-0.1/default) >= 0.1.2
Requires:       crate(rustfix-0.9/default) >= 0.9.2
Requires:       crate(same-file-1.0/default) >= 1.0.6
Requires:       crate(semver-1.0/default) >= 1.0.26
Requires:       crate(semver-1.0/serde) >= 1.0.26
Requires:       crate(serde-1.0/default) >= 1.0.219
Requires:       crate(serde-1.0/derive) >= 1.0.219
Requires:       crate(serde-ignored-0.1/default) >= 0.1.12
Requires:       crate(serde-json-1.0/default) >= 1.0.140
Requires:       crate(serde-json-1.0/raw-value) >= 1.0.140
Requires:       crate(serde-untagged-0.1/default) >= 0.1.7
Requires:       crate(sha1-0.10/default) >= 0.10.6
Requires:       crate(shell-escape-0.1/default) >= 0.1.5
Requires:       crate(supports-hyperlinks-3.0/default) >= 3.1.0
Requires:       crate(supports-unicode-3.0/default) >= 3.0.0
Requires:       crate(tar-0.4) >= 0.4.44
Requires:       crate(tempfile-3.0/default) >= 3.20.0
Requires:       crate(thiserror-2.0/default) >= 2.0.12
Requires:       crate(time-0.3/default) >= 0.3.41
Requires:       crate(time-0.3/formatting) >= 0.3.41
Requires:       crate(time-0.3/parsing) >= 0.3.41
Requires:       crate(time-0.3/serde) >= 0.3.41
Requires:       crate(toml-0.9/display) >= 0.9.0
Requires:       crate(toml-0.9/parse) >= 0.9.0
Requires:       crate(toml-0.9/preserve-order) >= 0.9.0
Requires:       crate(toml-0.9/serde) >= 0.9.0
Requires:       crate(toml-0.9/std) >= 0.9.0
Requires:       crate(toml-edit-0.23/default) >= 0.23.0
Requires:       crate(toml-edit-0.23/serde) >= 0.23.0
Requires:       crate(tracing-0.1/attributes) >= 0.1.41
Requires:       crate(tracing-0.1/std) >= 0.1.41
Requires:       crate(tracing-chrome-0.7/default) >= 0.7.2
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.19
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.19
Requires:       crate(unicase-2.0/default) >= 2.8.1
Requires:       crate(unicode-width-0.2/default) >= 0.2.1
Requires:       crate(unicode-xid-0.2/default) >= 0.2.6
Requires:       crate(url-2.0/default) >= 2.5.4
Requires:       crate(walkdir-2.0/default) >= 2.5.0
Requires:       crate(windows-sys-0.60/default) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-foundation) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-security) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-storage-filesystem) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-console) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-io) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-jobobjects) >= 0.60.0
Requires:       crate(windows-sys-0.60/win32-system-threading) >= 0.60.0
Provides:       crate(%{pkgname})

%description
Source code for takopackized Rust crate "cargo"

%package     -n %{name}+all-static
Summary:        Package manager for Rust - feature "all-static"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/vendored-libgit2)
Requires:       crate(%{pkgname}/vendored-openssl)
Requires:       crate(curl-0.4/force-system-lib-on-osx) >= 0.4.48
Requires:       crate(curl-0.4/http2) >= 0.4.48
Requires:       crate(curl-0.4/static-curl) >= 0.4.48
Provides:       crate(%{pkgname}/all-static)

%description -n %{name}+all-static
This metapackage enables feature "all-static" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+http-transport-curl
Summary:        Package manager for Rust - feature "http-transport-curl" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(gix-0.73/blocking-http-transport-curl) >= 0.73.0
Requires:       crate(gix-0.73/dirwalk) >= 0.73.0
Requires:       crate(gix-0.73/parallel) >= 0.73.0
Requires:       crate(gix-0.73/progress-tree) >= 0.73.0
Requires:       crate(gix-0.73/status) >= 0.73.0
Provides:       crate(%{pkgname}/default)
Provides:       crate(%{pkgname}/http-transport-curl)

%description -n %{name}+http-transport-curl
This metapackage enables feature "http-transport-curl" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%package     -n %{name}+http-transport-reqwest
Summary:        Package manager for Rust - feature "http-transport-reqwest"
Requires:       crate(%{pkgname})
Requires:       crate(gix-0.73/blocking-http-transport-reqwest) >= 0.73.0
Requires:       crate(gix-0.73/dirwalk) >= 0.73.0
Requires:       crate(gix-0.73/parallel) >= 0.73.0
Requires:       crate(gix-0.73/progress-tree) >= 0.73.0
Requires:       crate(gix-0.73/status) >= 0.73.0
Provides:       crate(%{pkgname}/http-transport-reqwest)

%description -n %{name}+http-transport-reqwest
This metapackage enables feature "http-transport-reqwest" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+openssl
Summary:        Package manager for Rust - feature "openssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-0.10/default) >= 0.10.73
Provides:       crate(%{pkgname}/openssl)

%description -n %{name}+openssl
This metapackage enables feature "openssl" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-libgit2
Summary:        Package manager for Rust - feature "vendored-libgit2"
Requires:       crate(%{pkgname})
Requires:       crate(libgit2-sys-0.18/vendored) >= 0.18.2
Provides:       crate(%{pkgname}/vendored-libgit2)

%description -n %{name}+vendored-libgit2
This metapackage enables feature "vendored-libgit2" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+vendored-openssl
Summary:        Package manager for Rust - feature "vendored-openssl"
Requires:       crate(%{pkgname})
Requires:       crate(openssl-0.10/vendored) >= 0.10.73
Provides:       crate(%{pkgname}/vendored-openssl)

%description -n %{name}+vendored-openssl
This metapackage enables feature "vendored-openssl" for the Rust cargo crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

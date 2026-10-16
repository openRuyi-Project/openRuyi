# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cargo-packager
Version:        0.11.8
Release:        %autorelease
Summary:        Executable packager and bundler for Rust applications
License:        Apache-2.0 OR MIT
URL:            https://github.com/crabnebula-dev/cargo-packager
#!RemoteAsset:  sha256:9aa0f5056c4191007702931dce47054c98fe78cbbebbaff8c7c39d5ebeed123d
Source0:        https://static.crates.io/crates/%{name}/%{name}-%{version}.crate
BuildSystem:    rust

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  help2man
BuildRequires:  crate(ar-0.9/default) >= 0.9.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(cargo-metadata-0.18/default) >= 0.18.0
BuildRequires:  crate(cargo-packager-utils-0.1/default) >= 0.1.1
BuildRequires:  crate(cargo-packager-utils-0.1/serde) >= 0.1.1
BuildRequires:  crate(clap-4/default) >= 4.5.0
BuildRequires:  crate(clap-4/derive) >= 4.5.0
BuildRequires:  crate(clap-4/env) >= 4.5.0
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(dunce-1/default) >= 1.0.0
BuildRequires:  crate(flate2-1/default) >= 1.0.0
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(handlebars-6/default) >= 6.0.0
BuildRequires:  crate(heck-0.5/default) >= 0.5.0
BuildRequires:  crate(hex-0.4/default) >= 0.4.0
BuildRequires:  crate(image-0.25) >= 0.25.0
BuildRequires:  crate(image-0.25/bmp) >= 0.25.0
BuildRequires:  crate(image-0.25/ico) >= 0.25.0
BuildRequires:  crate(image-0.25/jpeg) >= 0.25.0
BuildRequires:  crate(image-0.25/png) >= 0.25.0
BuildRequires:  crate(image-0.25/rayon) >= 0.25.0
BuildRequires:  crate(md5-0.7/default) >= 0.7.0
BuildRequires:  crate(minisign-0.7/default) >= 0.7.0
BuildRequires:  crate(native-tls-0.2/default) >= 0.2.0
BuildRequires:  crate(once-cell-1/default) >= 1.0.0
BuildRequires:  crate(openssl-src-300) >= 300.2.0
BuildRequires:  crate(os-pipe-1/default) >= 1.0.0
BuildRequires:  crate(plist-1/default) >= 1.0.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(relative-path-1/default) >= 1.9.0
BuildRequires:  crate(schemars-0.8/default) >= 0.8.0
BuildRequires:  crate(schemars-0.8/derive) >= 0.8.0
BuildRequires:  crate(schemars-0.8/preserve-order) >= 0.8.0
BuildRequires:  crate(schemars-0.8/url) >= 0.8.0
BuildRequires:  crate(semver-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(sha1-0.10/default) >= 0.10.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10.0
BuildRequires:  crate(strsim-0.11/default) >= 0.11.0
BuildRequires:  crate(tar-0.4/default) >= 0.4.0
BuildRequires:  crate(tauri-icns-0.1/default) >= 0.1.0
BuildRequires:  crate(tempfile-3/default) >= 3.0.0
BuildRequires:  crate(thiserror-1/default) >= 1.0.0
BuildRequires:  crate(time-0.3/default) >= 0.3.0
BuildRequires:  crate(time-0.3/formatting) >= 0.3.0
BuildRequires:  crate(toml-0.9/default) >= 0.9.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.0
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
BuildRequires:  crate(ureq-2) >= 2.10.0
BuildRequires:  crate(ureq-2/tls) >= 2.10.0
BuildRequires:  crate(uuid-1/default) >= 1.0.0
BuildRequires:  crate(uuid-1/v4) >= 1.0.0
BuildRequires:  crate(uuid-1/v5) >= 1.0.0
BuildRequires:  crate(walkdir-2/default) >= 2.0.0
BuildRequires:  crate(webpki-roots-1/default) >= 1.0.0
BuildRequires:  crate(windows-registry-0.5/default) >= 0.5.0
BuildRequires:  crate(windows-sys-0.52/win32-system-diagnostics-debug) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/win32-system-systeminformation) >= 0.52.0
BuildRequires:  crate(windows-sys-0.52/default) >= 0.52.0
BuildRequires:  crate(zip-0.6) >= 0.6.0
BuildRequires:  crate(zip-0.6/deflate) >= 0.6.0

Requires:       cargo

%description
Cargo-packager creates installers and application bundles from executables.
It supports Debian packages, AppImages, and Pacman packages on Linux, and can
read configuration from Packager.toml, JSON, or Cargo package metadata.

%install
install -Dm0755 target/release/cargo-packager %{buildroot}%{_bindir}/cargo-packager
install -d %{buildroot}%{_mandir}/man1
help2man --no-info --name='Package executables into installers and application bundles' \
    target/release/cargo-packager > %{buildroot}%{_mandir}/man1/cargo-packager.1

%files
%doc README.md CHANGELOG.md schema.json
%license LICENSE_APACHE-2.0 LICENSE_MIT
%{_bindir}/cargo-packager
%{_mandir}/man1/cargo-packager.1*

%changelog
%autochangelog

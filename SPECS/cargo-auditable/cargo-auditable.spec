# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           cargo-auditable
Version:        0.7.7
Release:        %autorelease
Summary:        Embed dependency metadata in Rust binaries
License:        MIT OR Apache-2.0
URL:            https://github.com/rust-secure-code/cargo-auditable
#!RemoteAsset:  sha256:ccdd489bc94d1338cd04389a842e00661300331ec915fb376b4810ef7d480b5d
Source0:        https://static.crates.io/crates/%{name}/%{version}/download#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:cab2a4b65cfde0734c98416740d24d4e3f03441ea8a0b385f0431e35244a05aa
Source1:        https://github.com/rust-secure-code/cargo-auditable/archive/refs/tags/v%{version}/%{name}-%{version}-upstream.tar.gz
BuildSystem:    rust

# The self-hosting test references the absent ../rust-audit-info workspace member.
# The WebAssembly test needs a wasm32 standard library unavailable in the build root.
# The target query test needs the ARM LLVM backend, absent from openRuyi rustc.
BuildOption(check):  --skip test_self_hosting --skip test_wasm --skip target_json::tests::query_linker_flavor --test-threads=1

BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(auditable-serde-0.9/default) >= 0.9.0
BuildRequires:  crate(auditable-info-0.10/default) >= 0.10.0
BuildRequires:  crate(auditable-info-0.10/wasm) >= 0.10.0
BuildRequires:  crate(cargo-metadata-0.23/default) >= 0.23.0
BuildRequires:  crate(miniz-oxide-0.9/default) >= 0.9.0
BuildRequires:  crate(object-0.37/write) >= 0.37.0
BuildRequires:  crate(pico-args-0.5/default) >= 0.5.0
BuildRequires:  crate(pico-args-0.5/eq-separator) >= 0.5.0
BuildRequires:  crate(pico-args-0.5/short-space-opt) >= 0.5.0
BuildRequires:  crate(serde-1/default) >= 1.0.147
BuildRequires:  crate(serde-1/derive) >= 1.0.219
BuildRequires:  crate(serde-json-1/default) >= 1.0.57
BuildRequires:  crate(wasm-gen-0.1/default) >= 0.1.4
BuildRequires:  crate(which-8/default) >= 8.0.0

Requires:       cargo
Requires:       rust

%description
Cargo auditable embeds a compressed list of Rust dependencies in a dedicated
section of each compiled binary. This metadata lets auditing tools identify
crate versions without access to the source tree or Cargo.lock.

%prep -a
mkdir upstream
tar -xzf %{SOURCE1} --strip-components=1 -C upstream
cp upstream/LICENSE-MIT upstream/LICENSE-APACHE .
cp -a upstream/cargo-auditable/tests/fixtures tests/
find tests/fixtures -name Cargo.lock -delete

%install
install -Dm0755 target/release/cargo-auditable %{buildroot}%{_bindir}/cargo-auditable
install -Dm0644 cargo-auditable.1 %{buildroot}%{_mandir}/man1/cargo-auditable.1

%check -p
export CARGO_NET_OFFLINE=true

%files
%doc README.md CHANGELOG.md
%license LICENSE-MIT LICENSE-APACHE
%{_bindir}/cargo-auditable
%{_mandir}/man1/cargo-auditable.1*

%changelog
%autochangelog

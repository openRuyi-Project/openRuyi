# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           pngquant
Version:        3.0.3
Release:        %autorelease
Summary:        Lossy PNG compressor
License:        GPL-3.0-or-later
URL:            https://pngquant.org
VCS:            git:https://github.com/kornelski/pngquant.git
#!RemoteAsset:  sha256:ddd8889a9c269ba454d0c5e4f7167948d55d77c4570b23f671809fd3a68b6822
Source:         https://github.com/kornelski/pngquant/archive/refs/tags/%{version}.tar.gz
BuildSystem:    rust

# Use registry crates and dynamically linked system image libraries on openRuyi.
Patch2000:      2000-Use-system-Rust-dependencies-on-openRuyi.patch
# Correct stale version and legacy C CLI assertions in the integration test.
Patch2001:      2001-Fix-stale-CLI-test-expectations.patch

BuildRequires:  cargo
BuildRequires:  pkgconfig(lcms2)
BuildRequires:  pkgconfig(libpng)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(cc-1/default) >= 1.0.72
BuildRequires:  crate(dunce-1/default) >= 1.0.4
BuildRequires:  crate(getopts-0.2/default) >= 0.2.21
BuildRequires:  crate(imagequant-sys-4/default) >= 4.0.3
BuildRequires:  crate(lcms2-sys-4/dynamic) >= 4.0.3
BuildRequires:  crate(libc-0.2/default) >= 0.2.112
BuildRequires:  crate(libpng-sys-1) >= 1.1.9
BuildRequires:  crate(libz-sys-1) >= 1.1.20
BuildRequires:  crate(wild-2/default) >= 2.2.0

%description
pngquant converts 24-bit and 32-bit PNG images to a more efficient 8-bit
palette format while preserving full alpha transparency. Its lossy
compression can substantially reduce file sizes while retaining visual
quality.

%install
install -Dpm0755 target/release/pngquant %{buildroot}%{_bindir}/pngquant
install -Dpm0644 pngquant.1 %{buildroot}%{_mandir}/man1/pngquant.1

%check
cargo test --offline
# test/test.c covers the separately packaged libimagequant C API and cannot be
# linked through Cargo's private dependency artifacts. Run pngquant's complete
# CLI integration suite and leave that provider-specific binary test to its
# owning crate.
bash test/test.sh test target/release/pngquant true

%files
%doc CHANGELOG README.md
%license COPYRIGHT
%{_bindir}/pngquant
%{_mandir}/man1/pngquant.1*

%changelog
%autochangelog

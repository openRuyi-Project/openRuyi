# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           agg
Version:        1.9.0
Release:        %autorelease
Summary:        asciinema gif generator
License:        GPL-3.0-only
URL:            https://docs.asciinema.org/manual/agg/
VCS:            git:https://github.com/asciinema/agg.git
#!RemoteAsset:  sha256:8170119502ad2c1c697e5cd4d050d87c425ecee726c5f6c3c2140703bcb31bb3
Source:         https://github.com/asciinema/agg/archive/refs/tags/v%{version}.tar.gz
BuildSystem:    rust

BuildRequires:  rust-rpm-macros
BuildRequires:  rust
BuildRequires:  cargo
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(avt-0.18/default) >= 0.18.0
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(env-logger-0.11/default) >= 0.11.10
BuildRequires:  crate(fontdb-0.23/default) >= 0.23.0
BuildRequires:  crate(gifski-1/default) >= 1.34.0
BuildRequires:  crate(imgref-1/default) >= 1.12.1
BuildRequires:  crate(jni-sys-0.4/default) >= 0.4.1
BuildRequires:  crate(log-0.4/default) >= 0.4.29
BuildRequires:  crate(reqwest-0.13/blocking) >= 0.13.3
BuildRequires:  crate(reqwest-0.13/gzip) >= 0.13.3
BuildRequires:  crate(reqwest-0.13/rustls) >= 0.13.3
BuildRequires:  crate(resvg-0.45/default) >= 0.45.1
BuildRequires:  crate(resvg-0.45/text) >= 0.45.1
BuildRequires:  crate(rgb-0.8/default) >= 0.8.53
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.149
BuildRequires:  crate(shellexpand-3/default) >= 3.1.2
BuildRequires:  crate(swash-0.2/default) >= 0.2.7
BuildRequires:  crate(tiny-skia-0.11/default) >= 0.11.4
BuildRequires:  crate(ttf-parser-0.25/default) >= 0.25.1
BuildRequires:  crate(usvg-0.45/default) >= 0.45.1

%description
agg is a command-line tool for generating animated GIF files from
terminal session recordings.

It supports conversion from asciicast files produced by asciinema
recorder. It uses Kornel Lesiński's excellent gifski library to
produce optimized, high quality GIF output with accurate frame timing.

%install
install -Dpm 0755 target/release/agg %{buildroot}%{_bindir}/agg

%files
%doc README.md
%license LICENSE
%{_bindir}/agg

%changelog
%autochangelog

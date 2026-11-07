# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname tensorboard-data-server

Name:           python-%{srcname}
Version:        0.7.2
Release:        %autorelease
Summary:        Native event data server for TensorBoard
License:        Apache-2.0
URL:            https://github.com/tensorflow/tensorboard
#!RemoteAsset:  sha256:02a510803df83cc66564964a0087adc6e2aabcb0b7617b7258b80e3115624bdd
Source0:        https://github.com/tensorflow/tensorboard/archive/refs/tags/data-server-v%{version}.tar.gz#/%{srcname}-%{version}.tar.gz
Patch2000:      2000-Use-the-stable-Clap-3-command-line-API.patch
BuildSystem:    pyproject

BuildOption(prep):  -n tensorboard-data-server-v%{version} -p1
BuildOption(install):  tensorboard_data_server

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
# TakoPack-generated dependencies.
BuildRequires:  crate(async-stream-0.3/default) >= 0.3.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.41
BuildRequires:  crate(base64-0.13/default) >= 0.13.0
BuildRequires:  crate(byteorder-1/default) >= 1.3.4
BuildRequires:  crate(bytes-1/default) >= 1.0.1
BuildRequires:  crate(clap-3/default) >= 3.2.25
BuildRequires:  crate(clap-3/derive) >= 3.2.25
BuildRequires:  crate(crc-1/default) >= 1.8.1
BuildRequires:  crate(crossbeam-0.8/default) >= 0.8.0
BuildRequires:  crate(env-logger-0.8/default) >= 0.8.2
BuildRequires:  crate(futures-core-0.3/default) >= 0.3.12
BuildRequires:  crate(gcp-auth-0.7/default) >= 0.7.4
BuildRequires:  crate(log-0.4/default) >= 0.4.11
BuildRequires:  crate(prost-0.9/default) >= 0.9.0
BuildRequires:  crate(prost-types-0.9/default) >= 0.9.0
BuildRequires:  crate(rand-0.7/default) >= 0.7.3
BuildRequires:  crate(rand-chacha-0.2/default) >= 0.2.2
BuildRequires:  crate(rayon-1/default) >= 1.5.0
BuildRequires:  crate(reqwest-0.11/blocking) >= 0.11.0
BuildRequires:  crate(reqwest-0.11/json) >= 0.11.0
BuildRequires:  crate(reqwest-0.11/rustls-tls) >= 0.11.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.59
BuildRequires:  crate(thiserror-1/default) >= 1.0.21
BuildRequires:  crate(tokio-1/default) >= 1.8.4
BuildRequires:  crate(tokio-1/macros) >= 1.8.4
BuildRequires:  crate(tokio-1/parking-lot) >= 1.8.4
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.8.4
BuildRequires:  crate(tokio-stream-0.1/default) >= 0.1.2
BuildRequires:  crate(tokio-stream-0.1/net) >= 0.1.2
BuildRequires:  crate(tonic-0.6/default) >= 0.6.2
BuildRequires:  crate(tonic-reflection-0.3/default) >= 0.3.0
BuildRequires:  crate(walkdir-2/default) >= 2.3.1

Provides:       python3-%{srcname} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Rust event-file data server and Python discovery interface used by
TensorBoard for efficient loading of training logs.

%generate_buildrequires
%pyproject_buildrequires

%prep -a
cp tensorboard/data/server/pip_package/setup.py .
cp -a tensorboard/data/server/pip_package/tensorboard_data_server .
pushd tensorboard/data/server
%rust_setup_registry
popd

%build -p
pushd tensorboard/data/server
export RUST_BUILD_ARGS="--bin rustboard"
%rust_build_release
popd
install -Dpm0755 tensorboard/data/server/target/release/rustboard tensorboard_data_server/bin/server

%files -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog

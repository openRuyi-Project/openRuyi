# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hf_xet

Name:           python-hf-xet
Version:        1.5.1
Release:        %autorelease
Summary:        Fast transfer layer for large files on Hugging Face Hub
License:        Apache-2.0
URL:            https://pypi.org/project/hf-xet/
VCS:            git:https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:51ef4500dab3764b41135ee1381a4b62ce56fc54d4c92b719b59e597d6df5bf6
Source0:        https://files.pythonhosted.org/packages/source/h/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop unused top-level workspace crates that are not built for this package.
Patch2000:      2000-fix-cargo-toml.patch

BuildOption(install):  hf_xet

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(pip)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(maturin)
BuildRequires:  cmake
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(pprof-0.14/protobuf-codec) >= 0.14
BuildRequires:  crate(pprof-0.14/inferno) >= 0.14
BuildRequires:  crate(pprof-0.14/prost) >= 0.14
BuildRequires:  crate(pprof-0.14/cpp) >= 0.14
BuildRequires:  crate(jni-sys-0.4) >= 0.4
BuildRequires:  crate(openssl-src-300) >= 300
BuildRequires:  crate(pyo3-0.26/indoc) >= 0.26
BuildRequires:  crate(pyo3-0.26/macros) >= 0.26
BuildRequires:  crate(pyo3-0.26/multiple-pymethods) >= 0.26
BuildRequires:  crate(console-subscriber-0.5) >= 0.5
BuildRequires:  crate(signal-hook-0.3) >= 0.3
BuildRequires:  crate(anyhow-1/default) >= 1.0.102
BuildRequires:  crate(approx-0.5/default) >= 0.5.1
BuildRequires:  crate(async-std-1/default) >= 1.13.2
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.89
BuildRequires:  crate(base64-0.22/default) >= 0.22.1
BuildRequires:  crate(blake3-1/default) >= 1.8.4
BuildRequires:  crate(bytemuck-1/default) >= 1.25.0
BuildRequires:  crate(bytes-1/default) >= 1.11.1
BuildRequires:  crate(chrono-0.4/default) >= 0.4.44
BuildRequires:  crate(clap-4/default) >= 4.6.1
BuildRequires:  crate(clap-4/derive) >= 4.6.1
BuildRequires:  crate(colored-3/default) >= 3.1.1
BuildRequires:  crate(const-str-1/default) >= 1.1.0
BuildRequires:  crate(countio-0.3/default) >= 0.3.0
BuildRequires:  crate(countio-0.3/futures) >= 0.3.0
BuildRequires:  crate(crc32fast-1/default) >= 1.5.0
BuildRequires:  crate(criterion-0.4/async-tokio) >= 0.4.0
BuildRequires:  crate(criterion-0.4/default) >= 0.4.0
BuildRequires:  crate(csv-1/default) >= 1.4.0
BuildRequires:  crate(ctor-1/default) >= 1.0.7
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.32
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.32
BuildRequires:  crate(gearhash-0.1/default) >= 0.1.3
BuildRequires:  crate(getrandom-0.4/default) >= 0.4.2
BuildRequires:  crate(getrandom-0.4/wasm-js) >= 0.4.2
BuildRequires:  crate(git-version-0.3/default) >= 0.3.9
BuildRequires:  crate(half-2/default) >= 2.7.1
BuildRequires:  crate(heapify-0.2/default) >= 0.2.0
BuildRequires:  crate(http-1/default) >= 1.4.0
BuildRequires:  crate(httpmock-0.8/default) >= 0.8.3
BuildRequires:  crate(humantime-2/default) >= 2.3.0
BuildRequires:  crate(hyper-1/default) >= 1.9.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(konst-0.4/default) >= 0.4.3
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.186
BuildRequires:  crate(lz4-flex-0.13/default) >= 0.13.1
BuildRequires:  crate(mockall-0.14/default) >= 0.14.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.1
BuildRequires:  crate(oneshot-0.1/default) >= 0.1.13
BuildRequires:  crate(pin-project-1/default) >= 1.1.10
BuildRequires:  crate(postcard-1/alloc) >= 1.1.3
BuildRequires:  crate(postcard-1/default) >= 1.1.3
BuildRequires:  crate(rand-0.10/default) >= 0.10.1
BuildRequires:  crate(rand-distr-0.6/default) >= 0.6.0
BuildRequires:  crate(redb-3/default) >= 3.1.3
BuildRequires:  crate(regex-1/default) >= 1.12.3
BuildRequires:  crate(hyper-tls-0.6/default) >= 0.6.0
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/rustls) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/socks) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.2
BuildRequires:  crate(reqwest-0.13/system-proxy) >= 0.13.2
BuildRequires:  crate(reqwest-middleware-0.5/default) >= 0.5.2
BuildRequires:  crate(safe-transmute-0.11/default) >= 0.11.3
BuildRequires:  crate(serde-1/default) >= 1.0.228
BuildRequires:  crate(serde-1/derive) >= 1.0.228
BuildRequires:  crate(serde-json-1/default) >= 1.0.150
BuildRequires:  crate(serde-repr-0.1/default) >= 0.1.20
BuildRequires:  crate(serial-test-3/default) >= 3.5.0
BuildRequires:  crate(sha2-0.10/asm) >= 0.10.9
BuildRequires:  crate(sha2-0.10/default) >= 0.10.9
BuildRequires:  crate(shellexpand-3/default) >= 3.1.2
BuildRequires:  crate(shellexpand-3/path) >= 3.1.2
BuildRequires:  crate(smol-2/default) >= 2.0.2
BuildRequires:  crate(static-assertions-1/default) >= 1.1.0
BuildRequires:  crate(statrs-0.18) >= 0.18.0
BuildRequires:  crate(sysinfo-0.38/default) >= 0.38.4
BuildRequires:  crate(tempfile-3/default) >= 3.27.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.18
BuildRequires:  crate(tokio-1/default) >= 1.52.3
BuildRequires:  crate(tokio-1/io-util) >= 1.52.3
BuildRequires:  crate(tokio-1/macros) >= 1.52.3
BuildRequires:  crate(tokio-1/net) >= 1.52.3
BuildRequires:  crate(tokio-1/rt) >= 1.52.3
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.52.3
BuildRequires:  crate(tokio-1/sync) >= 1.52.3
BuildRequires:  crate(tokio-1/test-util) >= 1.52.3
BuildRequires:  crate(tokio-1/time) >= 1.52.3
BuildRequires:  crate(tokio-retry-0.3/default) >= 0.3.2
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.18
BuildRequires:  crate(tokio-util-0.7/io) >= 0.7.18
BuildRequires:  crate(tracing-0.1/default) >= 0.1.44
BuildRequires:  crate(tracing-appender-0.2/default) >= 0.2.5
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.23
BuildRequires:  crate(tracing-subscriber-0.3/json) >= 0.3.23
BuildRequires:  crate(tracing-test-0.2/default) >= 0.2.6
BuildRequires:  crate(tracing-test-0.2/no-env-filter) >= 0.2.6
BuildRequires:  crate(url-2/default) >= 2.5.8
BuildRequires:  crate(urlencoding-2/default) >= 2.1.3
BuildRequires:  crate(uuid-1/default) >= 1.23.2
BuildRequires:  crate(uuid-1/js) >= 1.23.2
BuildRequires:  crate(uuid-1/v4) >= 1.23.2
BuildRequires:  crate(uuid-1/v7) >= 1.23.2
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(web-time-1/default) >= 1.1.0
BuildRequires:  crate(whoami-2/default) >= 2.1.2
BuildRequires:  crate(winapi-0.3/default) >= 0.3.9
BuildRequires:  crate(winapi-0.3/handleapi) >= 0.3.9
BuildRequires:  crate(winapi-0.3/processthreadsapi) >= 0.3.9
BuildRequires:  crate(winapi-0.3/securitybaseapi) >= 0.3.9
BuildRequires:  crate(winapi-0.3/winerror) >= 0.3.9
BuildRequires:  crate(winapi-0.3/winnt) >= 0.3.9
BuildRequires:  crate(wiremock-0.6/default) >= 0.6.5

Provides:       python3-hf-xet = %{version}-%{release}
Provides:       python3-hf-xet%{?_isa} = %{version}-%{release}
%python_provide python3-hf-xet

%description
Hf-xet provides fast transfer support for large model and dataset files in the
Hugging Face Hub ecosystem.

%prep -a
%rust_setup_registry
rm -rf hf_xet/Cargo.lock

%build -p
export CFLAGS="${CFLAGS} -O0 -Wp,-U_FORTIFY_SOURCE"
export CXXFLAGS="${CXXFLAGS} -O0 -Wp,-U_FORTIFY_SOURCE"

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md
%license hf_xet/LICENSE

%changelog
%autochangelog

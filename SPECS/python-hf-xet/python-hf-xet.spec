# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Gui-Yue <xiangwei.riscv@isrc.iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname hf_xet

Name:           python-hf-xet
Version:        1.5.2
Release:        %autorelease
Summary:        Fast transfer layer for large files on Hugging Face Hub
License:        Apache-2.0
URL:            https://pypi.org/project/hf-xet/
VCS:            git:https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:73044bd31bae33c984af832d19c752a0dffb67518fee9ddbd91d616e1101cf47
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
# Workspace member hf_xet.
# TakoPack-generated dependencies.
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(http-1/default) >= 1.0.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(pyo3-0.29/abi3-py38) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/auto-initialize) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(signal-hook-0.3/default) >= 0.3.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(winapi-0.3/consoleapi) >= 0.3.0
BuildRequires:  crate(winapi-0.3/default) >= 0.3.0
BuildRequires:  crate(winapi-0.3/errhandlingapi) >= 0.3.0
BuildRequires:  crate(winapi-0.3/wincon) >= 0.3.0
# Workspace member hf-xet.
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(http-1/default) >= 1.0.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokio-1/default) >= 1.49.0
BuildRequires:  crate(tokio-1/macros) >= 1.49.0
BuildRequires:  crate(tokio-1/net) >= 1.49.0
BuildRequires:  crate(tokio-1/rt) >= 1.49.0
BuildRequires:  crate(tokio-1/sync) >= 1.49.0
BuildRequires:  crate(tokio-1/time) >= 1.49.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-with-wasm-0.8/default) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/rt) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/sync) >= 0.8.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(uuid-1/default) >= 1.0.0
BuildRequires:  crate(uuid-1/v7) >= 1.0.0
# Workspace member hf-xet.
# TakoPack-generated dependencies for feature: python.
BuildRequires:  crate(pyo3-0.29/abi3-py38) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/multiple-pymethods) >= 0.29.0
# Workspace member xet-client.
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(crc32fast-1/default) >= 1.5.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(http-1/default) >= 1.0.0
BuildRequires:  crate(hyper-1/default) >= 1.8.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(redb-3/default) >= 3.1.0
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/socks) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/system-proxy) >= 0.13.1
BuildRequires:  crate(reqwest-middleware-0.5/default) >= 0.5.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(serde-repr-0.1/default) >= 0.1.0
BuildRequires:  crate(statrs-0.18) >= 0.18.0
BuildRequires:  crate(tempfile-3/default) >= 3.25.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokio-1/default) >= 1.49.0
BuildRequires:  crate(tokio-1/io-util) >= 1.49.0
BuildRequires:  crate(tokio-1/macros) >= 1.49.0
BuildRequires:  crate(tokio-1/rt) >= 1.49.0
BuildRequires:  crate(tokio-1/sync) >= 1.49.0
BuildRequires:  crate(tokio-1/time) >= 1.49.0
BuildRequires:  crate(tokio-retry-0.3/default) >= 0.3.0
BuildRequires:  crate(tokio-with-wasm-0.8/default) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/rt) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/sync) >= 0.8.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(urlencoding-2/default) >= 2.1.0
BuildRequires:  crate(web-time-1/default) >= 1.1.0
# Workspace member xet-client.
# TakoPack-generated dependencies for features: default, rustls-tls.
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/rustls) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/socks) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/system-proxy) >= 0.13.1
# Workspace member xet-core-structures.
# TakoPack-generated dependencies.
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(blake3-1/default) >= 1.8.0
BuildRequires:  crate(bytemuck-1/default) >= 1.0.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(countio-0.3/default) >= 0.3.0
BuildRequires:  crate(countio-0.3/futures) >= 0.3.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(futures-util-0.3/default) >= 0.3.0
BuildRequires:  crate(getrandom-0.4/default) >= 0.4.0
BuildRequires:  crate(getrandom-0.4/wasm-js) >= 0.4.0
BuildRequires:  crate(heapify-0.2/default) >= 0.2.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(lz4-flex-0.13/default) >= 0.13.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(regex-1/default) >= 1.0.0
BuildRequires:  crate(safe-transmute-0.11/default) >= 0.11.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(static-assertions-1/default) >= 1.1.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokio-1/default) >= 1.49.0
BuildRequires:  crate(tokio-1/io-util) >= 1.49.0
BuildRequires:  crate(tokio-1/macros) >= 1.49.0
BuildRequires:  crate(tokio-1/rt) >= 1.49.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.49.0
BuildRequires:  crate(tokio-1/sync) >= 1.49.0
BuildRequires:  crate(tokio-1/test-util) >= 1.49.0
BuildRequires:  crate(tokio-1/time) >= 1.49.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-util-0.7/io) >= 0.7.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(uuid-1/default) >= 1.0.0
BuildRequires:  crate(uuid-1/js) >= 1.0.0
BuildRequires:  crate(uuid-1/v4) >= 1.0.0
BuildRequires:  crate(web-time-1/default) >= 1.1.0
# Workspace member xet-runtime.
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(colored-3/default) >= 3.0.0
BuildRequires:  crate(const-str-1/default) >= 1.1.0
BuildRequires:  crate(ctor-1/default) >= 1.0.0
BuildRequires:  crate(dirs-6/default) >= 6.0.0
BuildRequires:  crate(futures-0.3/default) >= 0.3.0
BuildRequires:  crate(git-version-0.3/default) >= 0.3.0
BuildRequires:  crate(humantime-2/default) >= 2.1.0
BuildRequires:  crate(konst-0.4/default) >= 0.4.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(libc-0.2/default) >= 0.2.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.0
BuildRequires:  crate(oneshot-0.1/default) >= 0.1.0
BuildRequires:  crate(pin-project-1/default) >= 1.0.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(reqwest-0.13/json) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/socks) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/stream) >= 0.13.1
BuildRequires:  crate(reqwest-0.13/system-proxy) >= 0.13.1
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(shellexpand-3/default) >= 3.1.0
BuildRequires:  crate(shellexpand-3/path) >= 3.1.0
BuildRequires:  crate(sysinfo-0.38/default) >= 0.38.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokio-1/default) >= 1.49.0
BuildRequires:  crate(tokio-1/io-util) >= 1.49.0
BuildRequires:  crate(tokio-1/macros) >= 1.49.0
BuildRequires:  crate(tokio-1/rt) >= 1.49.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.49.0
BuildRequires:  crate(tokio-1/sync) >= 1.49.0
BuildRequires:  crate(tokio-1/test-util) >= 1.49.0
BuildRequires:  crate(tokio-1/time) >= 1.49.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-util-0.7/io) >= 0.7.0
BuildRequires:  crate(tokio-with-wasm-0.8/default) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/rt) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/sync) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/time) >= 0.8.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(tracing-appender-0.2/default) >= 0.2.0
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.0
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
BuildRequires:  crate(tracing-subscriber-0.3/json) >= 0.3.0
BuildRequires:  crate(web-time-1/default) >= 1.1.0
BuildRequires:  crate(whoami-2/default) >= 2.0.0
BuildRequires:  crate(winapi-0.3/default) >= 0.3.0
BuildRequires:  crate(winapi-0.3/handleapi) >= 0.3.0
BuildRequires:  crate(winapi-0.3/processthreadsapi) >= 0.3.0
BuildRequires:  crate(winapi-0.3/securitybaseapi) >= 0.3.0
BuildRequires:  crate(winapi-0.3/winerror) >= 0.3.0
BuildRequires:  crate(winapi-0.3/winnt) >= 0.3.0
# Workspace member xet-runtime.
# TakoPack-generated dependencies for feature: python.
BuildRequires:  crate(pyo3-0.29/abi3-py38) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/multiple-pymethods) >= 0.29.0
# Workspace member xet-data.
# TakoPack-generated dependencies.
BuildRequires:  crate(anyhow-1/default) >= 1.0.0
BuildRequires:  crate(async-trait-0.1/default) >= 0.1.0
BuildRequires:  crate(bytes-1/default) >= 1.11.0
BuildRequires:  crate(chrono-0.4/default) >= 0.4.0
BuildRequires:  crate(gearhash-0.1/default) >= 0.1.0
BuildRequires:  crate(http-1/default) >= 1.0.0
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(lazy-static-1/default) >= 1.5.0
BuildRequires:  crate(more-asserts-0.3/default) >= 0.3.0
BuildRequires:  crate(rand-0.10/default) >= 0.10.0
BuildRequires:  crate(serde-1/default) >= 1.0.0
BuildRequires:  crate(serde-1/derive) >= 1.0.0
BuildRequires:  crate(serde-json-1/default) >= 1.0.0
BuildRequires:  crate(sha2-0.10/asm) >= 0.10.0
BuildRequires:  crate(sha2-0.10/default) >= 0.10.0
BuildRequires:  crate(tempfile-3/default) >= 3.25.0
BuildRequires:  crate(thiserror-2/default) >= 2.0.0
BuildRequires:  crate(tokio-1/default) >= 1.49.0
BuildRequires:  crate(tokio-1/io-util) >= 1.49.0
BuildRequires:  crate(tokio-1/macros) >= 1.49.0
BuildRequires:  crate(tokio-1/rt) >= 1.49.0
BuildRequires:  crate(tokio-1/rt-multi-thread) >= 1.49.0
BuildRequires:  crate(tokio-1/sync) >= 1.49.0
BuildRequires:  crate(tokio-1/time) >= 1.49.0
BuildRequires:  crate(tokio-util-0.7/default) >= 0.7.0
BuildRequires:  crate(tokio-with-wasm-0.8/default) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/macros) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/rt) >= 0.8.0
BuildRequires:  crate(tokio-with-wasm-0.8/sync) >= 0.8.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.0
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(uuid-1/default) >= 1.0.0
BuildRequires:  crate(uuid-1/v7) >= 1.0.0
BuildRequires:  crate(web-time-1/default) >= 1.1.0
# Workspace member xet-data.
# TakoPack-generated dependencies for feature: python.
BuildRequires:  crate(pyo3-0.29/abi3-py38) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/default) >= 0.29.0
BuildRequires:  crate(pyo3-0.29/multiple-pymethods) >= 0.29.0
# Additional dependencies required by OBS builds.
# Offline cargo metadata resolves the optional profiler manifest during PEP 517 metadata generation.
# Upstream keeps pprof defaults, including the C++ demangler needed by offline resolution.
BuildRequires:  crate(pprof-0.14/default)
# The declared flamegraph feature supplies the inferno manifest to the resolver.
BuildRequires:  crate(pprof-0.14/flamegraph)
# Offline resolution also needs the selected prost and protobuf-codec dependencies.
BuildRequires:  crate(pprof-0.14/prost)
BuildRequires:  crate(pprof-0.14/protobuf-codec)
# Cargo resolves the xet-runtime console feature manifest even in a non-profiling wheel.
BuildRequires:  crate(console-subscriber-0.5)
# reqwest also resolves its optional native TLS manifest during offline metadata generation.
BuildRequires:  crate(hyper-tls-0.6)
# Cargo resolves the Android JNI branch of rustls-platform-verifier while creating metadata.
BuildRequires:  crate(jni-sys-0.4)
# The resolver reads openssl-sys optional source metadata. Neither Linux target enables vendored OpenSSL.
BuildRequires:  crate(openssl-src-300)

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

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name xet-runtime
%global full_version 1.5.2
%global pkgname xet-runtime-1

Name:           rust-xet-runtime-1
Version:        1.5.2
Release:        %autorelease
Summary:        Rust crate "xet-runtime"
License:        Apache-2.0
URL:            https://github.com/huggingface/xet-core
#!RemoteAsset:  sha256:15d8f121c33866f7648b737abe70d0e2dd9c0af4ffdd7219207531d0283aa63d
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(anyhow-1/default) >= 1.0.0
Requires:       crate(async-trait-0.1/default) >= 0.1.0
Requires:       crate(bytes-1/default) >= 1.11.0
Requires:       crate(chrono-0.4/default) >= 0.4.0
Requires:       crate(colored-3/default) >= 3.0.0
Requires:       crate(const-str-1/default) >= 1.1.0
Requires:       crate(ctor-0.6/default) >= 0.6.0
Requires:       crate(dirs-6/default) >= 6.0.0
Requires:       crate(futures-0.3/default) >= 0.3.0
Requires:       crate(git-version-0.3/default) >= 0.3.0
Requires:       crate(humantime-2/default) >= 2.1.0
Requires:       crate(konst-0.4/default) >= 0.4.0
Requires:       crate(lazy-static-1/default) >= 1.5.0
Requires:       crate(libc-0.2/default) >= 0.2.0
Requires:       crate(more-asserts-0.3/default) >= 0.3.0
Requires:       crate(oneshot-0.1/default) >= 0.1.0
Requires:       crate(pin-project-1/default) >= 1.0.0
Requires:       crate(rand-0.10/default) >= 0.10.0
Requires:       crate(reqwest-0.13/json) >= 0.13.1
Requires:       crate(reqwest-0.13/socks) >= 0.13.1
Requires:       crate(reqwest-0.13/stream) >= 0.13.1
Requires:       crate(reqwest-0.13/system-proxy) >= 0.13.1
Requires:       crate(serde-1/default) >= 1.0.0
Requires:       crate(serde-1/derive) >= 1.0.0
Requires:       crate(serde-json-1/default) >= 1.0.0
Requires:       crate(shellexpand-3/default) >= 3.1.0
Requires:       crate(shellexpand-3/path) >= 3.1.0
Requires:       crate(sysinfo-0.38/default) >= 0.38.0
Requires:       crate(thiserror-2/default) >= 2.0.0
Requires:       crate(tokio-1/default) >= 1.49.0
Requires:       crate(tokio-1/io-util) >= 1.49.0
Requires:       crate(tokio-1/macros) >= 1.49.0
Requires:       crate(tokio-1/rt) >= 1.49.0
Requires:       crate(tokio-1/rt-multi-thread) >= 1.49.0
Requires:       crate(tokio-1/sync) >= 1.49.0
Requires:       crate(tokio-1/test-util) >= 1.49.0
Requires:       crate(tokio-1/time) >= 1.49.0
Requires:       crate(tokio-util-0.7/default) >= 0.7.0
Requires:       crate(tokio-util-0.7/io) >= 0.7.0
Requires:       crate(tracing-0.1/default) >= 0.1.0
Requires:       crate(tracing-appender-0.2/default) >= 0.2.0
Requires:       crate(tracing-subscriber-0.3/default) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/env-filter) >= 0.3.0
Requires:       crate(tracing-subscriber-0.3/json) >= 0.3.0
Requires:       crate(whoami-2/default) >= 2.0.0
Requires:       crate(winapi-0.3/default) >= 0.3.0
Requires:       crate(winapi-0.3/handleapi) >= 0.3.0
Requires:       crate(winapi-0.3/processthreadsapi) >= 0.3.0
Requires:       crate(winapi-0.3/securitybaseapi) >= 0.3.0
Requires:       crate(winapi-0.3/winerror) >= 0.3.0
Requires:       crate(winapi-0.3/winnt) >= 0.3.0
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/elevated-information-level) = %{version}
Provides:       crate(%{pkgname}/fd-track) = %{version}
Provides:       crate(%{pkgname}/no-default-cache) = %{version}
Provides:       crate(%{pkgname}/simulation) = %{version}
Provides:       crate(%{pkgname}/smoke-test) = %{version}
Provides:       crate(%{pkgname}/strict) = %{version}

%description
Source code for takopackized Rust crate "xet-runtime"

%package     -n %{name}+python
Summary:        Async runtime, configuration, logging, and utility infrastructure for the Hugging Face Xet client tools - feature "python"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(pyo3-0.26/abi3-py37) >= 0.26.0
Requires:       crate(pyo3-0.26/default) >= 0.26.0
Requires:       crate(pyo3-0.26/multiple-pymethods) >= 0.26.0
Provides:       crate(%{pkgname}/python) = %{version}

%description -n %{name}+python
This metapackage enables feature "python" for the Rust xet-runtime crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+tokio-console
Summary:        Async runtime, configuration, logging, and utility infrastructure for the Hugging Face Xet client tools - feature "tokio-console"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(console-subscriber-0.5/default) >= 0.5.0
Provides:       crate(%{pkgname}/tokio-console) = %{version}

%description -n %{name}+tokio-console
This metapackage enables feature "tokio-console" for the Rust xet-runtime crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

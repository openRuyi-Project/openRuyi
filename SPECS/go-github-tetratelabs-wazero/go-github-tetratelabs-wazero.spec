# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: HNO3Miracle <xiangao.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%define _name           wazero
%define go_import_path  github.com/tetratelabs/wazero

Name:           go-github-tetratelabs-wazero
Version:        1.11.0
Release:        %autorelease
Summary:        wazero: the zero dependency WebAssembly runtime for Go developers
License:        Apache-2.0
URL:            https://github.com/tetratelabs/wazero
#!RemoteAsset:  sha256:a785f0eabe510e454a01e0d187675a913f96814d0c7e38c4717e03f6d5420ed4
Source0:        https://github.com/tetratelabs/wazero/archive/v%{version}.tar.gz#/%{_name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    golangmodules

BuildOption(prep):  -n wazero-1.11.0
# OBS filesystem returns EEXIST instead of ENOTEMPTY for rename-over-nonempty-dir
# cases in internal/sysfs tests; the rest of the package test suite still runs.
%define go_test_exclude github.com/tetratelabs/wazero/internal/sysfs

BuildRequires:  go
BuildRequires:  go-rpm-macros
BuildRequires:  go(golang.org/x/sys)
BuildRequires:  go(golang.org/x/sys/cpu)
BuildRequires:  go(golang.org/x/sys/unix)
BuildRequires:  go(golang.org/x/sys/windows)

Provides:       go(github.com/tetratelabs/wazero) = %{version}
Provides:       go(github.com/tetratelabs/wazero/api) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/logging) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/sock) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/sys) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/sysfs) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/table) = %{version}
Provides:       go(github.com/tetratelabs/wazero/experimental/wazerotest) = %{version}
Provides:       go(github.com/tetratelabs/wazero/imports/assemblyscript) = %{version}
Provides:       go(github.com/tetratelabs/wazero/imports/emscripten) = %{version}
Provides:       go(github.com/tetratelabs/wazero/imports/wasi_snapshot_preview1) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/assemblyscript) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/assemblyscript/logging) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/descriptor) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/emscripten) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/interpreter) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/backend) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/backend/isa/amd64) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/backend/isa/arm64) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/backend/regalloc) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/frontend) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/ssa) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/testcases) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/engine/wazevo/wazevoapi) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/expctxkeys) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/filecache) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/fsapi) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/fstest) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/ieee754) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/bench) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/engine) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/filecache) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/fuzzcases) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/libsodium) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/spectest) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/spectest/tail-call) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/spectest/threads) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/spectest/v1) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/spectest/v2) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/integration_test/stdlibs) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/internalapi) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/leb128) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/logging) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/moremath) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/platform) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/sock) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/sys) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/sysfs) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/binaryencoding) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/dwarftestdata) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/fs) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/hammer) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/maintester) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/nodiff) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/proxy) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/testing/require) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/u32) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/u64) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/version) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasip1) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasip1/logging) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasm) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasm/binary) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasmdebug) = %{version}
Provides:       go(github.com/tetratelabs/wazero/internal/wasmruntime) = %{version}
Provides:       go(github.com/tetratelabs/wazero/sys) = %{version}

Requires:       go(golang.org/x/sys)
Requires:       go(golang.org/x/sys/cpu)
Requires:       go(golang.org/x/sys/unix)
Requires:       go(golang.org/x/sys/windows)


%description
wazero: the zero dependency WebAssembly runtime for Go developers

[Image: Go Reference]
(https://pkg.go.dev/badge/github.com/tetratelabs/wazero.svg)
(https://pkg.go.dev/github.com/tetratelabs/wazero) [Image: License]
(https://img.shields.io/badge/License-Apache_2.0-blue.svg)
(https://opensource.org/licenses/Apache-2.0)

WebAssembly is a way to safely run code compiled in other languages.
Runtimes execute WebAssembly Modules (Wasm), which are most often
binaries with a .wasm extension.

%files
%doc README.md
%doc CONTRIBUTING.md
%license LICENSE
%license NOTICE
%{go_sys_gopath}/%{go_import_path}

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname maturin

Name:           python-%{srcname}
Version:        1.15.0
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
#!RemoteAsset:  sha256:94b26cc8e8aba61a5f2099715fe640e18c5f678e9a500408b38761263954228a
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop test-only dependencies to keep the offline build closure minimal.
Patch2000:      2000-fix-cargo.patch

BuildOption(install):  %{srcname}

# TakoPack-generated dependencies.
BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  crate(anyhow-1/default) >= 1.0.80
BuildRequires:  crate(base64-0.22/default) >= 0.22.0
BuildRequires:  crate(cargo-config2-0.1/default) >= 0.1.24
BuildRequires:  crate(cargo-metadata-0.23/default) >= 0.23.1
BuildRequires:  crate(cargo-options-0.8/default) >= 0.8.1
BuildRequires:  crate(cbindgen-0.29) >= 0.29.0
BuildRequires:  crate(cc-1/default) >= 1.0.88
BuildRequires:  crate(clap-4/default) >= 4.0.0
BuildRequires:  crate(clap-4/derive) >= 4.0.0
BuildRequires:  crate(clap-4/env) >= 4.0.0
BuildRequires:  crate(clap-4/unstable-styles) >= 4.0.0
BuildRequires:  crate(clap-4/wrap-help) >= 4.0.0
BuildRequires:  crate(dunce-1/default) >= 1.0.2
BuildRequires:  crate(fat-macho-0.4) >= 0.4.10
BuildRequires:  crate(flate2-1/default) >= 1.0.18
BuildRequires:  crate(fs-err-3/default) >= 3.0.0
BuildRequires:  crate(glob-0.3/default) >= 0.3.0
BuildRequires:  crate(goblin-0.10/default) >= 0.10.0
BuildRequires:  crate(ignore-0.4/default) >= 0.4.20
BuildRequires:  crate(indexmap-2/default) >= 2.2.3
BuildRequires:  crate(itertools-0.14/default) >= 0.14.0
BuildRequires:  crate(lddtree-0.5/default) >= 0.5.0
BuildRequires:  crate(memmap2-0.9/default) >= 0.9.9
BuildRequires:  crate(normpath-1/default) >= 1.1.1
BuildRequires:  crate(once-cell-1/default) >= 1.7.2
BuildRequires:  crate(path-slash-0.2/default) >= 0.2.1
BuildRequires:  crate(pep440-rs-0.7/default) >= 0.7.3
BuildRequires:  crate(pep440-rs-0.7/tracing) >= 0.7.3
BuildRequires:  crate(pep508-rs-0.9/default) >= 0.9.2
BuildRequires:  crate(pep508-rs-0.9/tracing) >= 0.9.2
BuildRequires:  crate(platform-info-2/default) >= 2.0.2
BuildRequires:  crate(pyo3-introspection-0.29/default) >= 0.29.0
BuildRequires:  crate(pyproject-toml-0.13/default) >= 0.13.5
BuildRequires:  crate(pyproject-toml-0.13/pep639-glob) >= 0.13.5
BuildRequires:  crate(python-pkginfo-0.6/default) >= 0.6.8
BuildRequires:  crate(reflink-copy-0.1/default) >= 0.1.29
BuildRequires:  crate(regex-1/default) >= 1.7.0
BuildRequires:  crate(rustc-version-0.4/default) >= 0.4.0
BuildRequires:  crate(rustflags-0.1/default) >= 0.1.6
BuildRequires:  crate(same-file-1/default) >= 1.0.6
BuildRequires:  crate(semver-1/default) >= 1.0.22
BuildRequires:  crate(serde-1/default) >= 1.0.197
BuildRequires:  crate(serde-1/derive) >= 1.0.197
BuildRequires:  crate(serde-json-1/default) >= 1.0.114
BuildRequires:  crate(sha2-0.11/default) >= 0.11.0
BuildRequires:  crate(tar-0.4/default) >= 0.4.46
BuildRequires:  crate(target-lexicon-0.13/default) >= 0.13.3
BuildRequires:  crate(tempfile-3/default) >= 3.2.0
BuildRequires:  crate(textwrap-0.16/default) >= 0.16.1
BuildRequires:  crate(thiserror-2/default) >= 2.0.3
BuildRequires:  crate(time-0.3/default) >= 0.3.17
BuildRequires:  crate(toml-1/default) >= 1.1.2
BuildRequires:  crate(toml-edit-0.25/default) >= 0.25.0
BuildRequires:  crate(tracing-0.1/default) >= 0.1.36
BuildRequires:  crate(tracing-subscriber-0.3/default) >= 0.3.20
BuildRequires:  crate(tracing-subscriber-0.3/env-filter) >= 0.3.20
BuildRequires:  crate(url-2/default) >= 2.5.0
BuildRequires:  crate(walkdir-2/default) >= 2.5.0
BuildRequires:  crate(zip-8/bzip2) >= 8.1.0
BuildRequires:  crate(zip-8/deflate) >= 8.1.0
BuildRequires:  crate(zip-8/lzma) >= 8.1.0
BuildRequires:  crate(zip-8/time) >= 8.1.0
BuildRequires:  crate(zip-8/zstd) >= 8.1.0
# Additional dependencies required by OBS builds.
BuildRequires:  rust
BuildRequires:  crate(arwen-0.0.5/default) >= 0.0.5
BuildRequires:  crate(bytesize-2/default) >= 2.2.0
BuildRequires:  crate(cargo-cyclonedx-0.5/default) >= 0.5.9
BuildRequires:  crate(cargo-xwin-0.23) >= 0.23.1
BuildRequires:  crate(cargo-zigbuild-0.23) >= 0.23.1
BuildRequires:  crate(clap-complete-command-0.6/default) >= 0.6.1
BuildRequires:  crate(configparser-3/default) >= 3.0.3
BuildRequires:  crate(dialoguer-0.12) >= 0.12.0
BuildRequires:  crate(keyring-3/apple-native) >= 3.6.3
BuildRequires:  crate(minijinja-2/default) >= 2.5.0
BuildRequires:  crate(native-tls-0.2/default) >= 0.2.8
BuildRequires:  crate(pretty-assertions-1/default) >= 1.3.0
BuildRequires:  crate(schemars-1/default) >= 1.0.4
BuildRequires:  crate(wild-2/default) >= 2.1.0
BuildRequires:  crate(arwen-codesign-0.0.1-alpha.1/default) >= 0.0.1-alpha.1
BuildRequires:  crate(keyring-3/linux-native) >= 3.6.3
BuildRequires:  crate(ureq-3/native-tls) >= 3.2.0
BuildRequires:  crate(ureq-3/multipart) >= 3.2.0
BuildRequires:  crate(ureq-3/rustls-webpki-roots) >= 3.2.0
BuildRequires:  crate(jni-sys-0.4/default) >= 0.4.0

Provides:       python3-%{srcname} = %{version}-%{release}
Provides:       python3-%{srcname}%{?_isa} = %{version}-%{release}
%python_provide python3-%{srcname}

%description
Build and publish crates with pyo3, rust-cpython and cffi bindings as
well as rust binaries as python packages.

%prep -a
mkdir -p ~/.cargo
cat > ~/.cargo/config.toml <<'EOF'
[source.crates-io]
replace-with = "system-registry"

[source.system-registry]
directory = "/usr/share/cargo/registry"
EOF
# The system Cargo directory source does not provide crates.io checksums.
# Strip upstream lockfile checksums before refreshing the lock.
sed -i '/^checksum = /d' Cargo.lock

%build -p
cargo update --offline
%ifarch riscv64
# Work around rustc/LLVM SIGSEGV on rva23/pico_itx while compiling
# large Rust crates such as regex-automata in release mode.
export RUST_MIN_STACK=16777216
export CARGO_PROFILE_RELEASE_OPT_LEVEL=1
export CARGO_PROFILE_RELEASE_CODEGEN_UNITS=256
%endif

%generate_buildrequires
%pyproject_buildrequires

%files -f %{pyproject_files}
%doc README.md Changelog.md
%license license-apache license-mit
%{_bindir}/maturin

%changelog
%autochangelog

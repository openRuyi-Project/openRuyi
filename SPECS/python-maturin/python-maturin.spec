# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global srcname maturin

Name:           python-%{srcname}
Version:        1.14.0
Release:        %autorelease
Summary:        Build and publish Rust crates as Python packages
License:        Apache-2.0 OR MIT
URL:            https://github.com/PyO3/maturin
#!RemoteAsset:  sha256:f7f82a6aca4a6c402bf00b99200be199d4874d04b9b9e74e825726a3478bba7f
Source0:        https://files.pythonhosted.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
BuildSystem:    pyproject

# Drop test-only dependencies to keep the offline build closure minimal.
Patch2000:      2000-fix-cargo.patch

BuildOption(install):  %{srcname}

BuildRequires:  pyproject-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(setuptools)
BuildRequires:  python3dist(setuptools-rust)
BuildRequires:  python3dist(pip)
BuildRequires:  rust
BuildRequires:  rust-rpm-macros
BuildRequires:  crate(adler2-2) >= 2.0.1
BuildRequires:  crate(aho-corasick-1) >= 1.1.4
BuildRequires:  crate(allocator-api2-0.2) >= 0.2.21
BuildRequires:  crate(anstream-1) >= 1.0.0
BuildRequires:  crate(anstyle-1) >= 1.0.14
BuildRequires:  crate(anstyle-parse-1) >= 1.0.0
BuildRequires:  crate(anstyle-query-1) >= 1.1.5
BuildRequires:  crate(anstyle-wincon-3) >= 3.0.11
BuildRequires:  crate(anyhow-1) >= 1.0.102
BuildRequires:  crate(ar-archive-writer-0.5) >= 0.5.2
BuildRequires:  crate(arwen-0.0.5) >= 0.0.5
BuildRequires:  crate(arwen-codesign-0.0.1-alpha.1) >= 0.0.1-alpha.1
BuildRequires:  crate(autocfg-1) >= 1.5.0
BuildRequires:  crate(base64-0.22) >= 0.22.1
BuildRequires:  crate(base64ct-1) >= 1.8.3
BuildRequires:  crate(bitflags-2) >= 2.13.0
BuildRequires:  crate(block-buffer-0.10) >= 0.10.4
BuildRequires:  crate(block-buffer-0.12) >= 0.12.0
BuildRequires:  crate(borrow-or-share-0.2) >= 0.2.4
BuildRequires:  crate(boxcar-0.2) >= 0.2.14
BuildRequires:  crate(bstr-1) >= 1.12.1
BuildRequires:  crate(bumpalo-3) >= 3.20.2
BuildRequires:  crate(byteorder-1) >= 1.5.0
BuildRequires:  crate(bytes-1) >= 1.11.1
BuildRequires:  crate(bytesize-2) >= 2.4.0
BuildRequires:  crate(bzip2-0.6) >= 0.6.1
BuildRequires:  crate(cab-0.6) >= 0.6.0
BuildRequires:  crate(camino-1) >= 1.2.2
BuildRequires:  crate(cargo-config2-0.1) >= 0.1.44
BuildRequires:  crate(cargo-cyclonedx-0.5) >= 0.5.9
BuildRequires:  crate(cargo-lock-10) >= 10.1.0
BuildRequires:  crate(cargo-metadata-0.18) >= 0.18.1
BuildRequires:  crate(cargo-metadata-0.23) >= 0.23.1
BuildRequires:  crate(cargo-options-0.7) >= 0.7.6
BuildRequires:  crate(cargo-platform-0.1) >= 0.1.9
BuildRequires:  crate(cargo-platform-0.3) >= 0.3.1
BuildRequires:  crate(cargo-xwin-0.22) >= 0.22.0
BuildRequires:  crate(cargo-zigbuild-0.22) >= 0.22.3
BuildRequires:  crate(cbindgen-0.29) >= 0.29.2
BuildRequires:  crate(cc-1) >= 1.2.63
BuildRequires:  crate(cesu8-1) >= 1.1.0
BuildRequires:  crate(cfb-0.14) >= 0.14.0
BuildRequires:  crate(cfg-if-1) >= 1.0.4
BuildRequires:  crate(charset-0.1) >= 0.1.5
BuildRequires:  crate(chumsky-0.13) >= 0.13.0
BuildRequires:  crate(clap-4) >= 4.6.1
BuildRequires:  crate(clap-builder-4) >= 4.6.0
BuildRequires:  crate(clap-complete-4) >= 4.6.3
BuildRequires:  crate(clap-complete-command-0.6) >= 0.6.1
BuildRequires:  crate(clap-complete-nushell-4) >= 4.6.0
BuildRequires:  crate(clap-derive-4) >= 4.6.1
BuildRequires:  crate(clap-lex-1) >= 1.1.0
BuildRequires:  crate(cli-table-0.5) >= 0.5.0
BuildRequires:  crate(colorchoice-1) >= 1.0.5
BuildRequires:  crate(combine-4) >= 4.6.7
BuildRequires:  crate(configparser-3) >= 3.2.0
BuildRequires:  crate(console-0.16) >= 0.16.1
BuildRequires:  crate(const-oid-0.10) >= 0.10.2
BuildRequires:  crate(cookie-0.18) >= 0.18.1
BuildRequires:  crate(cookie-store-0.22) >= 0.22.1
BuildRequires:  crate(core-foundation-0.10) >= 0.10.1
BuildRequires:  crate(core-foundation-0.9) >= 0.9.4
BuildRequires:  crate(core-foundation-sys-0.8) >= 0.8.7
BuildRequires:  crate(cpufeatures-0.2) >= 0.2.17
BuildRequires:  crate(cpufeatures-0.3) >= 0.3.0
BuildRequires:  crate(crc32fast-1) >= 1.5.0
BuildRequires:  crate(crc-3) >= 3.4.0
BuildRequires:  crate(crc-catalog-2) >= 2.5.0
BuildRequires:  crate(crossbeam-channel-0.5) >= 0.5.15
BuildRequires:  crate(crossbeam-deque-0.8) >= 0.8.6
BuildRequires:  crate(crossbeam-epoch-0.9) >= 0.9.18
BuildRequires:  crate(crossbeam-utils-0.8) >= 0.8.21
BuildRequires:  crate(crypto-common-0.1) >= 0.1.6
BuildRequires:  crate(crypto-common-0.2) >= 0.2.2
BuildRequires:  crate(cyclonedx-bom-0.8) >= 0.8.1
BuildRequires:  crate(cyclonedx-bom-macros-0.1) >= 0.1.0
BuildRequires:  crate(data-encoding-2) >= 2.11.0
BuildRequires:  crate(der-0.8) >= 0.8.0
BuildRequires:  crate(deranged-0.5) >= 0.5.8
BuildRequires:  crate(dialoguer-0.12) >= 0.12.0
BuildRequires:  crate(diff-0.1) >= 0.1.13
BuildRequires:  crate(digest-0.10) >= 0.10.7
BuildRequires:  crate(digest-0.11) >= 0.11.3
BuildRequires:  crate(dirs-6) >= 6.0.0
BuildRequires:  crate(dirs-sys-0.5) >= 0.5.0
BuildRequires:  crate(displaydoc-0.2) >= 0.2.5
BuildRequires:  crate(document-features-0.2) >= 0.2.12
BuildRequires:  crate(dunce-1) >= 1.0.5
BuildRequires:  crate(dyn-clone-1) >= 1.0.20
BuildRequires:  crate(either-1) >= 1.16.0
BuildRequires:  crate(encode-unicode-1) >= 1.0.0
BuildRequires:  crate(encoding-rs-0.8) >= 0.8.35
BuildRequires:  crate(env-logger-0.10) >= 0.10.2
BuildRequires:  crate(equivalent-1) >= 1.0.2
BuildRequires:  crate(errno-0.3) >= 0.3.14
BuildRequires:  crate(fastrand-2) >= 2.4.1
BuildRequires:  crate(fat-macho-0.4) >= 0.4.11
BuildRequires:  crate(filetime-0.2) >= 0.2.27
BuildRequires:  crate(find-msvc-tools-0.1) >= 0.1.9
BuildRequires:  crate(flate2-1) >= 1.1.9
BuildRequires:  crate(fluent-uri-0.4) >= 0.4.1
BuildRequires:  crate(fnv-1) >= 1.0.7
BuildRequires:  crate(foldhash-0.1) >= 0.1.5
BuildRequires:  crate(foldhash-0.2) >= 0.2.0
BuildRequires:  crate(foreign-types-0.3) >= 0.3.2
BuildRequires:  crate(foreign-types-shared-0.1) >= 0.1.1
BuildRequires:  crate(form-urlencoded-1) >= 1.2.2
BuildRequires:  crate(fs-err-3) >= 3.3.0
BuildRequires:  crate(futures-core-0.3) >= 0.3.32
BuildRequires:  crate(futures-task-0.3) >= 0.3.32
BuildRequires:  crate(futures-util-0.3) >= 0.3.32
BuildRequires:  crate(generic-array-0.14) >= 0.14.9
BuildRequires:  crate(getrandom-0.2) >= 0.2.17
BuildRequires:  crate(getrandom-0.3) >= 0.3.4
BuildRequires:  crate(getrandom-0.4) >= 0.4.2
BuildRequires:  crate(glob-0.3) >= 0.3.3
BuildRequires:  crate(globset-0.4) >= 0.4.18
BuildRequires:  crate(goblin-0.10) >= 0.10.7
BuildRequires:  crate(hashbrown-0.15) >= 0.15.5
BuildRequires:  crate(hashbrown-0.16) >= 0.16.1
BuildRequires:  crate(hashbrown-0.17) >= 0.17.0
BuildRequires:  crate(heck-0.5) >= 0.5.0
BuildRequires:  crate(hermit-abi-0.5) >= 0.5.2
BuildRequires:  crate(hex-0.4) >= 0.4.3
BuildRequires:  crate(http-1) >= 1.4.0
BuildRequires:  crate(httparse-1) >= 1.10.1
BuildRequires:  crate(humantime-2) >= 2.3.0
BuildRequires:  crate(hybrid-array-0.4) >= 0.4.11
BuildRequires:  crate(icu-collections-2) >= 2.2.0
BuildRequires:  crate(icu-locale-core-2) >= 2.2.0
BuildRequires:  crate(icu-normalizer-2) >= 2.2.0
BuildRequires:  crate(icu-normalizer-data-2) >= 2.2.0
BuildRequires:  crate(icu-properties-2) >= 2.2.0
BuildRequires:  crate(icu-properties-data-2) >= 2.2.0
BuildRequires:  crate(icu-provider-2) >= 2.2.0
BuildRequires:  crate(id-arena-2) >= 2.3.0
BuildRequires:  crate(idna-1) >= 1.1.0
BuildRequires:  crate(idna-adapter-1) >= 1.2.1
BuildRequires:  crate(ignore-0.4) >= 0.4.25
BuildRequires:  crate(indexmap-2) >= 2.14.0
BuildRequires:  crate(indicatif-0.18) >= 0.18.4
BuildRequires:  crate(is-terminal-0.4) >= 0.4.17
BuildRequires:  crate(is-terminal-polyfill-1) >= 1.70.2
BuildRequires:  crate(itertools-0.13) >= 0.13.0
BuildRequires:  crate(itertools-0.14) >= 0.14.0
BuildRequires:  crate(itoa-1) >= 1.0.18
BuildRequires:  crate(jni-0.21) >= 0.21.1
BuildRequires:  crate(jni-sys-0.3) >= 0.3.1
BuildRequires:  crate(jni-sys-0.4) >= 0.4.1
BuildRequires:  crate(jni-sys-macros-0.4) >= 0.4.1
BuildRequires:  crate(jobserver-0.1) >= 0.1.34
BuildRequires:  crate(js-sys-0.3) >= 0.3.98
BuildRequires:  crate(keyring-3) >= 3.6.3
BuildRequires:  crate(lazy-static-1) >= 1.5.0
BuildRequires:  crate(lddtree-0.5) >= 0.5.0
BuildRequires:  crate(leb128fmt-0.1) >= 0.1.0
BuildRequires:  crate(libbz2-rs-sys-0.2) >= 0.2.5
BuildRequires:  crate(libc-0.2) >= 0.2.186
BuildRequires:  crate(libmimalloc-sys-0.1) >= 0.1.49
BuildRequires:  crate(libredox-0.1) >= 0.1.17
BuildRequires:  crate(linux-keyutils-0.2) >= 0.2.5
BuildRequires:  crate(linux-raw-sys-0.12) >= 0.12.1
BuildRequires:  crate(litemap-0.8) >= 0.8.2
BuildRequires:  crate(litrs-1) >= 1.0.0
BuildRequires:  crate(lock-api-0.4) >= 0.4.14
BuildRequires:  crate(log-0.4) >= 0.4.30
BuildRequires:  crate(lzma-rust2-0.16) >= 0.16.4
BuildRequires:  crate(lzma-sys-0.1) >= 0.1.20
BuildRequires:  crate(lzxd-0.2) >= 0.2.6
BuildRequires:  crate(mailparse-0.16) >= 0.16.1
BuildRequires:  crate(matchers-0.2) >= 0.2.0
BuildRequires:  crate(memchr-2) >= 2.8.1
BuildRequires:  crate(memmap2-0.9) >= 0.9.10
BuildRequires:  crate(memo-map-0.3) >= 0.3.3
BuildRequires:  crate(mimalloc-0.1) >= 0.1.52
BuildRequires:  crate(mime-0.3) >= 0.3.17
BuildRequires:  crate(mime-guess-2) >= 2.0.5
BuildRequires:  crate(minijinja-2) >= 2.20.0
BuildRequires:  crate(miniz-oxide-0.8) >= 0.8.9
BuildRequires:  crate(msi-0.10) >= 0.10.0
BuildRequires:  crate(native-tls-0.2) >= 0.2.18
BuildRequires:  crate(nom-8) >= 8.0.0
BuildRequires:  crate(normpath-1) >= 1.5.0
BuildRequires:  crate(nu-ansi-term-0.50) >= 0.50.3
BuildRequires:  crate(num-conv-0.2) >= 0.2.1
BuildRequires:  crate(num-traits-0.2) >= 0.2.19
BuildRequires:  crate(object-0.37) >= 0.37.3
BuildRequires:  crate(object-0.38) >= 0.38.1
BuildRequires:  crate(once-cell-1) >= 1.21.4
BuildRequires:  crate(once-cell-polyfill-1) >= 1.70.2
BuildRequires:  crate(openssl-0.10) >= 0.10.76
BuildRequires:  crate(openssl-macros-0.1) >= 0.1.1
BuildRequires:  crate(openssl-probe-0.1) >= 0.1.6
BuildRequires:  crate(openssl-probe-0.2) >= 0.2.1
BuildRequires:  crate(openssl-sys-0.9) >= 0.9.115
BuildRequires:  crate(option-ext-0.2) >= 0.2.0
BuildRequires:  crate(ordered-float-5) >= 5.3.0
BuildRequires:  crate(parking-lot-0.12) >= 0.12.5
BuildRequires:  crate(parking-lot-core-0.9) >= 0.9.12
BuildRequires:  crate(paste-1) >= 1.0.15
BuildRequires:  crate(pathdiff-0.2) >= 0.2.3
BuildRequires:  crate(path-slash-0.2) >= 0.2.1
BuildRequires:  crate(pem-rfc7468-1) >= 1.0.0
BuildRequires:  crate(pep440-rs-0.7) >= 0.7.3
BuildRequires:  crate(pep508-rs-0.9) >= 0.9.2
BuildRequires:  crate(percent-encoding-2) >= 2.3.2
BuildRequires:  crate(phf-0.11) >= 0.11.3
BuildRequires:  crate(phf-generator-0.11) >= 0.11.3
BuildRequires:  crate(phf-macros-0.11) >= 0.11.3
BuildRequires:  crate(phf-shared-0.11) >= 0.11.3
BuildRequires:  crate(pin-project-lite-0.2) >= 0.2.17
BuildRequires:  crate(pkg-config-0.3) >= 0.3.33
BuildRequires:  crate(plain-0.2) >= 0.2.3
BuildRequires:  crate(platform-info-2) >= 2.1.0
BuildRequires:  crate(portable-atomic-1) >= 1.13.1
BuildRequires:  crate(potential-utf-0.1) >= 0.1.5
BuildRequires:  crate(powerfmt-0.2) >= 0.2.0
BuildRequires:  crate(pretty-assertions-1) >= 1.4.1
BuildRequires:  crate(prettyplease-0.2) >= 0.2.37
BuildRequires:  crate(proc-macro2-1) >= 1.0.106
BuildRequires:  crate(psm-0.1) >= 0.1.31
BuildRequires:  crate(purl-0.1) >= 0.1.6
BuildRequires:  crate(pyo3-introspection-0.28) >= 0.28.3
BuildRequires:  crate(pyproject-toml-0.13) >= 0.13.7
BuildRequires:  crate(python-pkginfo-0.6) >= 0.6.8
BuildRequires:  crate(quote-1) >= 1.0.45
BuildRequires:  crate(quoted-printable-0.5) >= 0.5.2
BuildRequires:  crate(rand-0.8) >= 0.8.6
BuildRequires:  crate(rand-core-0.6) >= 0.6.4
BuildRequires:  crate(rayon-1) >= 1.12.0
BuildRequires:  crate(rayon-core-1) >= 1.13.0
BuildRequires:  crate(redox-syscall-0.5) >= 0.5.18
BuildRequires:  crate(redox-syscall-0.8) >= 0.8.0
BuildRequires:  crate(redox-users-0.5) >= 0.5.2
BuildRequires:  crate(ref-cast-1) >= 1.0.25
BuildRequires:  crate(ref-cast-impl-1) >= 1.0.25
BuildRequires:  crate(r-efi-5) >= 5.3.0
BuildRequires:  crate(r-efi-6) >= 6.0.0
BuildRequires:  crate(reflink-copy-0.1) >= 0.1.29
BuildRequires:  crate(regex-1) >= 1.12.3
BuildRequires:  crate(regex-automata-0.4) >= 0.4.14
BuildRequires:  crate(regex-syntax-0.8) >= 0.8.10
BuildRequires:  crate(rfc2047-decoder-1) >= 1.1.2
BuildRequires:  crate(ring-0.17) >= 0.17.14
BuildRequires:  crate(rustc-hash-2) >= 2.1.2
BuildRequires:  crate(rustc-version-0.4) >= 0.4.1
BuildRequires:  crate(rustflags-0.1) >= 0.1.7
BuildRequires:  crate(rustix-1) >= 1.1.4
BuildRequires:  crate(rustls-0.23) >= 0.23.37
BuildRequires:  crate(rustls-native-certs-0.8) >= 0.8.1
BuildRequires:  crate(rustls-pki-types-1) >= 1.14.0
BuildRequires:  crate(rustls-platform-verifier-0.6) >= 0.6.2
BuildRequires:  crate(rustls-platform-verifier-android-0.1) >= 0.1.1
BuildRequires:  crate(rustls-webpki-0.103) >= 0.103.10
BuildRequires:  crate(rustversion-1) >= 1.0.22
BuildRequires:  crate(ruzstd-0.8) >= 0.8.3
BuildRequires:  crate(same-file-1) >= 1.0.6
BuildRequires:  crate(schannel-0.1) >= 0.1.29
BuildRequires:  crate(schemars-1) >= 1.2.1
BuildRequires:  crate(schemars-derive-1) >= 1.2.1
BuildRequires:  crate(scopeguard-1) >= 1.2.0
BuildRequires:  crate(scroll-0.13) >= 0.13.0
BuildRequires:  crate(scroll-derive-0.13) >= 0.13.1
BuildRequires:  crate(security-framework-2) >= 2.11.1
BuildRequires:  crate(security-framework-3) >= 3.7.0
BuildRequires:  crate(security-framework-sys-2) >= 2.17.0
BuildRequires:  crate(semver-1) >= 1.0.28
BuildRequires:  crate(serde-1) >= 1.0.228
BuildRequires:  crate(serde-core-1) >= 1.0.228
BuildRequires:  crate(serde-derive-1) >= 1.0.228
BuildRequires:  crate(serde-derive-internals-0.29) >= 0.29.1
BuildRequires:  crate(serde-json-1) >= 1.0.150
BuildRequires:  crate(serde-spanned-0.6) >= 0.6.9
BuildRequires:  crate(serde-spanned-1) >= 1.1.1
BuildRequires:  crate(sha2-0.10) >= 0.10.9
BuildRequires:  crate(sha2-0.11) >= 0.11.0
BuildRequires:  crate(sharded-slab-0.1) >= 0.1.7
BuildRequires:  crate(shell-words-1) >= 1.1.1
BuildRequires:  crate(shlex-2) >= 2.0.1
BuildRequires:  crate(simd-adler32-0.3) >= 0.3.9
BuildRequires:  crate(siphasher-1) >= 1.0.3
BuildRequires:  crate(slab-0.4) >= 0.4.12
BuildRequires:  crate(smallvec-1) >= 1.15.1
BuildRequires:  crate(smawk-0.3) >= 0.3.2
BuildRequires:  crate(socks-0.3) >= 0.3.4
BuildRequires:  crate(spdx-0.13) >= 0.13.4
BuildRequires:  crate(stable-deref-trait-1) >= 1.2.1
BuildRequires:  crate(stacker-0.1) >= 0.1.24
BuildRequires:  crate(strsim-0.11) >= 0.11.1
BuildRequires:  crate(strum-0.28) >= 0.28.0
BuildRequires:  crate(strum-macros-0.28) >= 0.28.0
BuildRequires:  crate(subtle-2) >= 2.6.1
BuildRequires:  crate(syn-2) >= 2.0.117
BuildRequires:  crate(synstructure-0.13) >= 0.13.2
BuildRequires:  crate(tar-0.4) >= 0.4.46
BuildRequires:  crate(target-lexicon-0.13) >= 0.13.5
BuildRequires:  crate(tempfile-3) >= 3.27.0
BuildRequires:  crate(termcolor-1) >= 1.4.1
BuildRequires:  crate(terminal-size-0.4) >= 0.4.4
BuildRequires:  crate(textwrap-0.16) >= 0.16.2
BuildRequires:  crate(thiserror-1) >= 1.0.69
BuildRequires:  crate(thiserror-2) >= 2.0.18
BuildRequires:  crate(thiserror-impl-1) >= 1.0.69
BuildRequires:  crate(thiserror-impl-2) >= 2.0.18
BuildRequires:  crate(thread-local-1) >= 1.1.9
BuildRequires:  crate(time-0.3) >= 0.3.47
BuildRequires:  crate(time-core-0.1) >= 0.1.8
BuildRequires:  crate(time-macros-0.2) >= 0.2.27
BuildRequires:  crate(tinystr-0.8) >= 0.8.3
BuildRequires:  crate(toml-0.8) >= 0.8.23
BuildRequires:  crate(toml-0.9) >= 0.9.12
BuildRequires:  crate(toml-1) >= 1.1.2
BuildRequires:  crate(toml-datetime-0.6) >= 0.6.11
BuildRequires:  crate(toml-datetime-0.7) >= 0.7.5
BuildRequires:  crate(toml-datetime-1) >= 1.1.1
BuildRequires:  crate(toml-edit-0.22) >= 0.22.27
BuildRequires:  crate(toml-edit-0.25) >= 0.25.12
BuildRequires:  crate(toml-parser-1) >= 1.1.2
BuildRequires:  crate(toml-write-0.1) >= 0.1.2
BuildRequires:  crate(toml-writer-1) >= 1.1.1
BuildRequires:  crate(tracing-0.1) >= 0.1.44
BuildRequires:  crate(tracing-attributes-0.1) >= 0.1.31
BuildRequires:  crate(tracing-core-0.1) >= 0.1.36
BuildRequires:  crate(tracing-log-0.2) >= 0.2.0
BuildRequires:  crate(tracing-serde-0.2) >= 0.2.0
BuildRequires:  crate(tracing-subscriber-0.3) >= 0.3.23
BuildRequires:  crate(twox-hash-2) >= 2.1.2
BuildRequires:  crate(typed-path-0.12) >= 0.12.3
BuildRequires:  crate(typenum-1) >= 1.20.1
BuildRequires:  crate(unicase-2) >= 2.9.0
BuildRequires:  crate(unicode-ident-1) >= 1.0.24
BuildRequires:  crate(unicode-linebreak-0.1) >= 0.1.5
BuildRequires:  crate(unicode-segmentation-1) >= 1.13.2
BuildRequires:  crate(unicode-width-0.2) >= 0.2.2
BuildRequires:  crate(unicode-xid-0.2) >= 0.2.6
BuildRequires:  crate(unit-prefix-0.5) >= 0.5.2
BuildRequires:  crate(unscanny-0.1) >= 0.1.0
BuildRequires:  crate(untrusted-0.9) >= 0.9.0
BuildRequires:  crate(ureq-3) >= 3.3.0
BuildRequires:  crate(ureq-proto-0.6) >= 0.6.0
BuildRequires:  crate(url-2) >= 2.5.8
BuildRequires:  crate(urlencoding-2) >= 2.1.3
BuildRequires:  crate(utf8-iter-1) >= 1.0.4
BuildRequires:  crate(utf8parse-0.2) >= 0.2.2
BuildRequires:  crate(utf8-zero-0.8) >= 0.8.1
BuildRequires:  crate(uuid-1) >= 1.23.2
BuildRequires:  crate(validator-0.19) >= 0.19.0
BuildRequires:  crate(valuable-0.1) >= 0.1.1
BuildRequires:  crate(vcpkg-0.2) >= 0.2.15
BuildRequires:  crate(version-check-0.9) >= 0.9.5
BuildRequires:  crate(version-ranges-0.1) >= 0.1.3
BuildRequires:  crate(versions-7) >= 7.0.0
BuildRequires:  crate(walkdir-2) >= 2.5.0
BuildRequires:  crate(wasi-0.11) >= 0.11.1
BuildRequires:  crate(wasip2-1) >= 1.0.3
BuildRequires:  crate(wasip3-0.4) >= 0.4.0
BuildRequires:  crate(wasm-bindgen-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-macro-support-0.2) >= 0.2.121
BuildRequires:  crate(wasm-bindgen-shared-0.2) >= 0.2.121
BuildRequires:  crate(wasm-encoder-0.244) >= 0.244.0
BuildRequires:  crate(wasm-metadata-0.244) >= 0.244.0
BuildRequires:  crate(wasmparser-0.244) >= 0.244.0
BuildRequires:  crate(webpki-root-certs-1) >= 1.0.7
BuildRequires:  crate(webpki-roots-1) >= 1.0.5
BuildRequires:  crate(web-time-1) >= 1.1.0
BuildRequires:  crate(which-8) >= 8.0.2
BuildRequires:  crate(wild-2) >= 2.2.1
BuildRequires:  crate(winapi-0.3) >= 0.3.9
BuildRequires:  crate(winapi-i686-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(winapi-util-0.1) >= 0.1.11
BuildRequires:  crate(winapi-x86-64-pc-windows-gnu-0.4) >= 0.4.0
BuildRequires:  crate(windows-0.62) >= 0.62.2
BuildRequires:  crate(windows-aarch64-gnullvm-0.42) >= 0.42.2
BuildRequires:  crate(windows-aarch64-gnullvm-0.52) >= 0.52.6
BuildRequires:  crate(windows-aarch64-gnullvm-0.53) >= 0.53.1
BuildRequires:  crate(windows-aarch64-msvc-0.42) >= 0.42.2
BuildRequires:  crate(windows-aarch64-msvc-0.52) >= 0.52.6
BuildRequires:  crate(windows-aarch64-msvc-0.53) >= 0.53.1
BuildRequires:  crate(windows-collections-0.3) >= 0.3.2
BuildRequires:  crate(windows-core-0.62) >= 0.62.2
BuildRequires:  crate(windows-future-0.3) >= 0.3.2
BuildRequires:  crate(windows-i686-gnu-0.42) >= 0.42.2
BuildRequires:  crate(windows-i686-gnu-0.52) >= 0.52.6
BuildRequires:  crate(windows-i686-gnu-0.53) >= 0.53.1
BuildRequires:  crate(windows-i686-gnullvm-0.52) >= 0.52.6
BuildRequires:  crate(windows-i686-gnullvm-0.53) >= 0.53.1
BuildRequires:  crate(windows-i686-msvc-0.42) >= 0.42.2
BuildRequires:  crate(windows-i686-msvc-0.52) >= 0.52.6
BuildRequires:  crate(windows-i686-msvc-0.53) >= 0.53.1
BuildRequires:  crate(windows-implement-0.60) >= 0.60.2
BuildRequires:  crate(windows-interface-0.59) >= 0.59.3
BuildRequires:  crate(windows-link-0.2) >= 0.2.1
BuildRequires:  crate(windows-numerics-0.3) >= 0.3.1
BuildRequires:  crate(windows-result-0.4) >= 0.4.1
BuildRequires:  crate(windows-strings-0.5) >= 0.5.1
BuildRequires:  crate(windows-sys-0.45) >= 0.45.0
BuildRequires:  crate(windows-sys-0.52) >= 0.52.0
BuildRequires:  crate(windows-sys-0.59) >= 0.59.0
BuildRequires:  crate(windows-sys-0.60) >= 0.60.2
BuildRequires:  crate(windows-sys-0.61) >= 0.61.2
BuildRequires:  crate(windows-targets-0.42) >= 0.42.2
BuildRequires:  crate(windows-targets-0.52) >= 0.52.6
BuildRequires:  crate(windows-targets-0.53) >= 0.53.5
BuildRequires:  crate(windows-threading-0.2) >= 0.2.1
BuildRequires:  crate(windows-x86-64-gnu-0.42) >= 0.42.2
BuildRequires:  crate(windows-x86-64-gnu-0.52) >= 0.52.6
BuildRequires:  crate(windows-x86-64-gnu-0.53) >= 0.53.1
BuildRequires:  crate(windows-x86-64-gnullvm-0.42) >= 0.42.2
BuildRequires:  crate(windows-x86-64-gnullvm-0.52) >= 0.52.6
BuildRequires:  crate(windows-x86-64-gnullvm-0.53) >= 0.53.1
BuildRequires:  crate(windows-x86-64-msvc-0.42) >= 0.42.2
BuildRequires:  crate(windows-x86-64-msvc-0.52) >= 0.52.6
BuildRequires:  crate(windows-x86-64-msvc-0.53) >= 0.53.1
BuildRequires:  crate(winnow-0.7) >= 0.7.15
BuildRequires:  crate(winnow-1) >= 1.0.3
BuildRequires:  crate(wit-bindgen-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-0.57) >= 0.57.1
BuildRequires:  crate(wit-bindgen-core-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-rust-0.51) >= 0.51.0
BuildRequires:  crate(wit-bindgen-rust-macro-0.51) >= 0.51.0
BuildRequires:  crate(wit-component-0.244) >= 0.244.0
BuildRequires:  crate(wit-parser-0.244) >= 0.244.0
BuildRequires:  crate(writeable-0.6) >= 0.6.2
BuildRequires:  crate(xattr-1) >= 1.6.1
BuildRequires:  crate(xml-rs-0.8) >= 0.8.28
BuildRequires:  crate(xwin-0.9) >= 0.9.0
BuildRequires:  crate(xz2-0.1) >= 0.1.7
BuildRequires:  crate(yansi-1) >= 1.0.1
BuildRequires:  crate(yoke-0.8) >= 0.8.2
BuildRequires:  crate(yoke-derive-0.8) >= 0.8.2
BuildRequires:  crate(zerofrom-0.1) >= 0.1.7
BuildRequires:  crate(zerofrom-derive-0.1) >= 0.1.7
BuildRequires:  crate(zeroize-1) >= 1.8.2
BuildRequires:  crate(zerotrie-0.2) >= 0.2.4
BuildRequires:  crate(zerovec-0.11) >= 0.11.6
BuildRequires:  crate(zerovec-derive-0.11) >= 0.11.3
BuildRequires:  crate(zip-7) >= 7.2.0
BuildRequires:  crate(zip-8) >= 8.6.0
BuildRequires:  crate(zlib-rs-0.6) >= 0.6.3
BuildRequires:  crate(zmij-1) >= 1.0.21
BuildRequires:  crate(zopfli-0.8) >= 0.8.3
BuildRequires:  crate(zstd-0.13) >= 0.13.3
BuildRequires:  crate(zstd-safe-7) >= 7.2.4
BuildRequires:  crate(zstd-sys-2) >= 2.0.16

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
%license license-apache license-mit
%doc README.md Changelog.md
%{_bindir}/maturin

%changelog
%autochangelog

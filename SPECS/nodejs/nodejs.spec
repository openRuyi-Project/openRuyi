# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# Enabling LTO will cause the compilation to fail.
%global _lto_cflags           %{nil}
# Show build output without waiting for a Make target to finish.
%global _make_output_sync     %{nil}
%global toolchain             clang
%global _test_target          test-ci-js
%global nodejs_major          26
%global nodejs_minor          13
%global nodejs_patch          0
%global nodejs_abi            %{nodejs_major}.%{nodejs_minor}
%global nodejs_soversion      147
%global nodejs_version        %{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}

%global v8_major              14
%global v8_minor              6
%global v8_build              202
%global v8_patch              34
%global v8_abi                %{v8_major}.%{v8_minor}
%global v8_version            %{v8_major}.%{v8_minor}.%{v8_build}.%{v8_patch}

%global punycode_version      2.1.0
%global npm_version           11.20.0

Name:           nodejs
Version:        %{nodejs_version}
Release:        %autorelease
Summary:        JavaScript runtime
License:        Apache-2.0 AND Artistic-2.0 AND BSD-2-Clause AND BSD-3-Clause AND BlueOak-1.0.0 AND CC-BY-3.0 AND CC0-1.0 AND ISC AND MIT AND Unicode-3.0
URL:            https://nodejs.org/
VCS:            git:https://github.com/nodejs/node
#!RemoteAsset:  sha256:263f639ecfa7a17b49438d76cdbf9aff73179e3c7cb789da69b900718427fa2e
Source0:        https://nodejs.org/dist/v%{version}/node-v%{version}.tar.xz
Source1:        nodejs_native.attr
BuildSystem:    autotools

BuildOption(build):  NINJA_ARGS="%{__ninja_common_opts} node"
BuildOption(install):  NINJA_ARGS="%{__ninja_common_opts} node"
BuildOption(check):  JOBS="$RPM_BUILD_NCPUS"
%ifarch riscv64
# Exclude the unstable snapshot byte comparison; https://issues.chromium.org/issues/460332153.
BuildOption(check):  CI_SKIP_TESTS=parallel/test-snapshot-reproducible
%endif

BuildRequires:  chrpath
BuildRequires:  clang >= 19.1
BuildRequires:  rust >= 1.86
BuildRequires:  cargo >= 1.86
BuildRequires:  make >= 3.81
BuildRequires:  ninja
BuildRequires:  pkgconfig(ada)
BuildRequires:  pkgconfig(openssl) >= 3.5.1
BuildRequires:  pkgconfig(icu-i18n) >= 73
BuildRequires:  pkgconfig(libbrotlidec) >= 1.2.1
BuildRequires:  pkgconfig(libbrotlienc) >= 1.2.1
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libffi)
BuildRequires:  pkgconfig(LIEF)
BuildRequires:  pkgconfig(libhwy)
BuildRequires:  pkgconfig(libllhttp)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(simdjson)
BuildRequires:  pkgconfig(sqlite3) >= 3.54.0
BuildRequires:  pkgconfig(simdutf)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python-rpm-macros
BuildRequires:  pkgconfig(python3)
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(setuptools)

Provides:       nodejs(abi%{nodejs_major}) = %{nodejs_abi}
Provides:       nodejs(abi) = %{nodejs_abi}
Provides:       nodejs(engine) = %{version}
Provides:       nodejs(v8-abi%{v8_major}) = %{v8_abi}
Provides:       nodejs(v8-abi) = %{v8_abi}
Provides:       nodejs-punycode = %{punycode_version}
Provides:       npm(punycode) = %{punycode_version}

Obsoletes:      %{name}-libs < %{version}-%{release}
Recommends:     npm%{?_isa} >= %{npm_version}-%{release}

Requires:       ca-certificates
Requires:       brotli%{?_isa} >= 1.2.1
# The shared SQLite must provide RBU and Geopoly.
Requires:       sqlite%{?_isa} >= 3.54.0

%patchlist
# Preserve RISC-V live registers; https://github.com/v8/v8/commit/7e40e4bee05bbecad063f618ec64d48aa3a63ca7.
1000-v8-riscv-byteswap.patch
# Use public RISC-V float min/max helpers; https://github.com/v8/v8/commit/7d081be20f980a472a3460027d78423dd7efe603.
1001-v8-riscv-maglev-float-minmax.patch
# Use full-range RISC-V Wasm lazy jumps; https://github.com/v8/v8/commit/def38dd3f8726ed595932624ee5d681a3f02ed4a.
1002-v8-riscv-lazy-jump.patch
# Correct RISC-V vector register group sizes; https://github.com/v8/v8/commit/634bfd45341b92a639944687e1f9468687484b0e.
1003-v8-riscv-lmul.patch
# Correct half-width SIMD groups for VLEN 256 and 512; https://github.com/v8/v8/commit/cac8aa44a153889da1ee8542a503339f17f3a1cd.
1004-v8-riscv-half-lmul.patch
# Fix RISC-V floating-point comparisons; https://github.com/v8/v8/commit/8521e2e77535a5c255d15ff8deb459fc7260c54d.
1005-v8-riscv-fp-comparison.patch
# Handle ICU 79 case folding; https://github.com/v8/v8/commit/f607706154eabc4a949628a88b38dbe95cd2274c.
1006-v8-icu79-case-folding.patch
# Adapt the version test for zlib-ng compatibility; https://github.com/nodejs/node/blob/v26.12.0/test/parallel/test-process-versions.js.
2002-zlib-ng-version-test.patch
# Report unsupported Wasm SIMD as skipped; https://github.com/felixonmars/archriscv-packages/blob/2c56f9918e59cb5cfb7af860d2336785d0a36dea/nodejs/wasm-simd-skip.patch.
2003-wpt-wasm-simd-skip.patch
# Accept CLDR 49 date and time-zone formats; https://github.com/unicode-org/cldr/pull/5725 and https://github.com/unicode-org/cldr/pull/5783.
2004-test-cldr49-date-formats.patch

%description
Node.js is a platform built on Chrome's JavaScript runtime for easily building fast, scalable network applications. Node.js uses an event-driven, non-blocking I/O model that makes it lightweight and efficient, perfect for data-intensive real-time applications that run across distributed devices.

%package        devel
Summary:        JavaScript runtime - development headers
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig(openssl)
Requires:       pkgconfig(zlib)
Requires:       pkgconfig(libbrotlidec)
Requires:       pkgconfig(libuv)

%description    devel
Development headers for the Node.js JavaScript runtime.

%package     -n npm
Summary:        Node.js Package Manager
Version:        %{npm_version}
Provides:       npm = %{npm_version}
Provides:       npm(npm) = %{npm_version}
Recommends:     %{name}-docs = %{nodejs_version}-%{release}
Requires:       %{name}%{?_isa} = %{nodejs_version}-%{release}

%description -n npm
npm is a package manager for node.js. It manages dependencies and can install/publish your node programs.

%package        docs
Summary:        Node.js API documentation
BuildArch:      noarch

%description    docs
The API documentation for the Node.js JavaScript runtime.

%prep -a
rm -rf deps/brotli
rm -rf deps/cares
rm -rf deps/icu-small
rm -rf deps/LIEF
rm -rf deps/uv
rm -rf deps/zlib
rm -rf deps/zstd
rm -rf deps/simdjson
rm -rf deps/v8/third_party/simdutf

%conf
# Node.js uses GYP instead of GNU configure.
%set_build_flags
%{__python3} configure.py --prefix=%{_prefix} \
           --verbose \
           --ninja \
           --shared \
           --libdir=%{_lib} \
           --shared-ada \
           --shared-brotli \
           --shared-cares \
           --shared-ffi \
           --shared-highway \
           --shared-http-parser \
           --shared-libuv \
           --shared-lief \
           --shared-nghttp2 \
           --shared-openssl \
           --shared-simdjson \
           --shared-simdutf \
           --shared-sqlite \
           --shared-zlib \
           --shared-zstd \
           --with-intl=system-icu \
           --v8-enable-temporal-support \
           --openssl-use-def-ca-store

%build -p
%set_build_flags

%install -a
chmod 0755 %{buildroot}/%{_bindir}/node
chrpath --delete %{buildroot}%{_bindir}/node
ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/libnode.so

mkdir -p %{buildroot}%{_prefix}/lib/node_modules

install -Dpm0644 %{SOURCE1} %{buildroot}%{_rpmconfigdir}/fileattrs/nodejs_native.attr
cat << EOF > %{buildroot}%{_rpmconfigdir}/nodejs_native.req
#!/bin/sh
echo 'nodejs(abi%{nodejs_major}) >= %nodejs_abi'
echo 'nodejs(v8-abi%{v8_major}) >= %v8_abi'
EOF
chmod 0755 %{buildroot}%{_rpmconfigdir}/nodejs_native.req

mkdir -p %{buildroot}%{_pkgdocdir}/html
cp -pr doc/* %{buildroot}%{_pkgdocdir}/html
rm -f %{buildroot}%{_pkgdocdir}/html/nodejs.1

mkdir -p %{buildroot}%{_datadir}/node
cp -p common.gypi %{buildroot}%{_datadir}/node

mv %{buildroot}/%{_datadir}/doc/node/gdbinit %{buildroot}/%{_pkgdocdir}/gdbinit

mkdir -p %{buildroot}%{_mandir} \
         %{buildroot}%{_pkgdocdir}/npm

cp -pr deps/npm/man/* %{buildroot}%{_mandir}/
rm -rf %{buildroot}%{_prefix}/lib/node_modules/npm/man
ln -sf %{_mandir}  %{buildroot}%{_prefix}/lib/node_modules/npm/man

cp -pr deps/npm/docs %{buildroot}%{_pkgdocdir}/npm/
rm -rf %{buildroot}%{_prefix}/lib/node_modules/npm/docs

ln -sf %{_pkgdocdir}/npm/docs %{buildroot}%{_prefix}/lib/node_modules/npm/docs

rm -f %{buildroot}/%{_defaultdocdir}/node/lldb_commands.py \
      %{buildroot}/%{_defaultdocdir}/node/lldbinit

find %{buildroot}%{_prefix}/lib/node_modules/npm \
    -not -path "%{buildroot}%{_prefix}/lib/node_modules/npm/bin/*" \
    -executable -type f \
    -exec chmod -x {} \;

chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin/node-gyp
chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js

mkdir -p %{buildroot}%{_sysconfdir}
touch %{buildroot}%{_sysconfdir}/npmrc

%check -p
# Match the upstream test library layout; https://github.com/nodejs/node/blob/v26.12.1/test/common/shared-lib-util.js.
ln -sfn lib/libnode.so.%{nodejs_soversion} out/Release/libnode.so.%{nodejs_soversion}
export LD_LIBRARY_PATH="$PWD/out/Release${LD_LIBRARY_PATH:+:$LD_LIBRARY_PATH}"

%files
%doc %{_mandir}/man1/node.1*
%doc CHANGELOG.md onboarding.md GOVERNANCE.md README.md
%license LICENSE
%dir %{_datadir}/node
%dir %{_prefix}/lib/node_modules
%{_bindir}/node
%{_libdir}/libnode.so.%{nodejs_soversion}
%{_rpmconfigdir}/fileattrs/nodejs_native.attr
%{_rpmconfigdir}/nodejs_native.req

%files devel
%{_includedir}/node
%{_libdir}/libnode.so
%{_datadir}/node/common.gypi
%{_pkgdocdir}/gdbinit

%files -n npm
%{_bindir}/npm
%{_bindir}/npx
%{_prefix}/lib/node_modules/npm
%config(noreplace) %{_sysconfdir}/npmrc
%ghost %{_sysconfdir}/npmignore
%doc %{_mandir}/man*/
%exclude %doc %{_mandir}/man1/node.1*

%files docs
%dir %{_pkgdocdir}
%doc doc
%{_pkgdocdir}/html
%{_pkgdocdir}/npm/docs

%changelog
%autochangelog

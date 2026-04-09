# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

# Enabling LTO will cause the compilation to fail.
%global _lto_cflags           %{nil}
%global nodejs_major          24
%global nodejs_minor          13
%global nodejs_patch          0
%global nodejs_abi            %{nodejs_major}.%{nodejs_minor}
%global nodejs_soversion      137
%global nodejs_version        %{nodejs_major}.%{nodejs_minor}.%{nodejs_patch}

%global v8_major              13
%global v8_minor              6
%global v8_build              233
%global v8_patch              17
%global v8_abi                %{v8_major}.%{v8_minor}
%global v8_version            %{v8_major}.%{v8_minor}.%{v8_build}.%{v8_patch}

%global punycode_version      2.1.0
%global npm_version           11.6.2

%global uvwasi_version        0.0.23
%global histogram_version     0.11.9

Name:           nodejs
Version:        %{nodejs_version}
Release:        %autorelease
Summary:        JavaScript runtime
License:        MIT AND Apache-2.0 AND ISC AND BSD AND AFL-2.1
URL:            https://nodejs.org/
VCS:            git:https://github.com/nodejs/node
#!RemoteAsset:  sha256:320fe909cbb347dcf516201e4964ef177b8138df9a7f810d0d54950481b3158b
Source0:        https://nodejs.org/dist/v%{version}/node-v%{version}.tar.xz
Source1:        nodejs_native.attr
BuildSystem:    autotools

# Disable RVV in highway due to broken and disabled RVV runtime dispatch.
# patch from https://github.com/felixonmars/archriscv-packages/blob/e94cabe9480fb92bc732070d815eb03434838c54/nodejs/hwy-broken-rvv.diff
Patch0:         hwy-broken-rvv.diff
Patch1:         v8-riscv-fix-trampoline.patch
Patch2:         v8-riscv-fix-trampoline-release.patch
# patch from https://github.com/nodejs/node/pull/61666
Patch3:         v8-riscv-fix-sp.patch
# from https://github.com/felixonmars/archriscv-packages/blob/master/nodejs-lts-krypton/{60588,60591}.diff
Patch4:         60588.diff
Patch5:         60591.diff

BuildRequires:  chrpath
BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(openssl)
BuildRequires:  pkgconfig(icu-i18n)
BuildRequires:  pkgconfig(libbrotlidec)
BuildRequires:  pkgconfig(libcares)
BuildRequires:  pkgconfig(libllhttp)
BuildRequires:  pkgconfig(libnghttp2)
BuildRequires:  pkgconfig(libnghttp3)
BuildRequires:  pkgconfig(libuv)
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(simdjson)
# TODO: Using the shared simdutf will cause an npm segmentation fault, and it
# needs to be investigated.
# BuildRequires:  pkgconfig(simdutf)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  python-rpm-macros
# Used by configure.py
BuildRequires:  python3
BuildRequires:  python3dist(jinja2)
BuildRequires:  python3dist(setuptools)

Requires:       ca-certificates
Recommends:     npm%{?_isa} >= %{npm_version}-%{release}

Provides:  nodejs(abi%{nodejs_major}) = %{nodejs_abi}
Provides:  nodejs(abi) = %{nodejs_abi}
Provides:  nodejs(engine) = %{version}
Provides:  nodejs(v8-abi%{v8_major}) = %{v8_abi}
Provides:  nodejs(v8-abi) = %{v8_abi}
Provides:  nodejs-punycode = %{punycode_version}
Provides:  npm(punycode) = %{punycode_version}

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

%package        libs
Summary:        Node.js and V8 libraries

%description    libs
Libraries to support Node.js and provide stable V8 interfaces.

%package     -n npm
Summary:        Node.js Package Manager
Version:        %{npm_version}
Provides:       npm = %{npm_version}
Provides:       npm(npm) = %{npm_version}
Requires:       %{name}%{?_isa} = %{nodejs_version}-%{release}
Recommends:     %{name}-docs = %{nodejs_version}-%{release}

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
rm -rf deps/uv
rm -rf deps/zlib
rm -rf deps/zstd
rm -rf deps/simdjson

%conf
%set_build_flags
%{__python3} configure.py --prefix=%{_prefix} \
           --verbose \
           --shared \
           --libdir=%{_lib} \
           --shared-brotli \
           --shared-cares \
           --shared-http-parser \
           --shared-libuv \
           --shared-nghttp2 \
           --shared-nghttp3 \
           --shared-openssl \
           --shared-simdjson \
           --shared-sqlite \
           --shared-zlib \
           --shared-zstd \
           --with-intl=system-icu \
           --without-corepack \
           --openssl-use-def-ca-store

%install -a
chmod 0755 %{buildroot}/%{_bindir}/node
chrpath --delete %{buildroot}%{_bindir}/node
ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/libnode.so

for header in %{buildroot}%{_includedir}/node/libplatform %{buildroot}%{_includedir}/node/v8*.h; do
    header=$(basename ${header})
    ln -s ./node/${header} %{buildroot}%{_includedir}/${header}
done
ln -s ./node/cppgc %{buildroot}%{_includedir}/cppgc
for soname in libv8 libv8_libbase libv8_libplatform; do
    ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/${soname}.so
    ln -s libnode.so.%{nodejs_soversion} %{buildroot}%{_libdir}/${soname}.so.%{v8_major}
done

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

ln -sf %{_pkgdocdir}/npm %{buildroot}%{_prefix}/lib/node_modules/npm/docs

rm -f %{buildroot}/%{_defaultdocdir}/node/lldb_commands.py \
      %{buildroot}/%{_defaultdocdir}/node/lldbinit

find %{buildroot}%{_prefix}/lib/node_modules/npm \
    -not -path "%{buildroot}%{_prefix}/lib/node_modules/npm/bin/*" \
    -executable -type f \
    -exec chmod -x {} \;

chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/@npmcli/run-script/lib/node-gyp-bin/node-gyp
chmod 0755 %{buildroot}%{_prefix}/lib/node_modules/npm/node_modules/node-gyp/bin/node-gyp.js

mkdir -p %{buildroot}%{_sysconfdir}
touch %{SOURCE1} %{buildroot}%{_sysconfdir}/npmrc

# TODO: Make tests pass.
%check

%files
%dir %{_datadir}/node
%dir %{_prefix}/lib/node_modules
%doc %{_mandir}/man1/node.1*
%doc CHANGELOG.md onboarding.md GOVERNANCE.md README.md
%{_bindir}/node
%{_rpmconfigdir}/fileattrs/nodejs_native.attr
%{_rpmconfigdir}/nodejs_native.req

%files devel
%{_includedir}/node
%{_libdir}/libnode.so
%{_datadir}/node/common.gypi
%{_pkgdocdir}/gdbinit
%{_includedir}/libplatform
%{_includedir}/v8*.h
%{_libdir}/libv8.so
%{_includedir}/cppgc
%{_libdir}/libv8_libbase.so
%{_libdir}/libv8_libplatform.so

%files libs
%license LICENSE
%{_libdir}/libnode.so.%{nodejs_soversion}
%{_libdir}/libv8.so.%{v8_major}
%{_libdir}/libv8_libbase.so.%{v8_major}
%{_libdir}/libv8_libplatform.so.%{v8_major}

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

# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nss
Version:        3.115
Release:        %autorelease
Summary:        Network Security Services
License:        MPL-2.0
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
VCS:            hg:https://hg.mozilla.org/projects/nss
#!RemoteAsset
Source:         https://ftp.mozilla.org/pub/security/nss/releases/NSS_3_115_RTM/src/nss-3.115-with-nspr-4.37.tar.gz
BuildSystem:    autotools

BuildOption(build):  -C nss
BuildOption(build):  nss_build_all
BuildOption(build):  BUILD_OPT=1
BuildOption(build):  NSS_USE_SYSTEM_SQLITE=1
BuildOption(build):  NSS_ENABLE_WERROR=0
BuildOption(build):  USE_64=1

BuildRequires:  gcc-c++
BuildRequires:  make
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(zlib)
BuildRequires:  perl
BuildRequires:  which

%description
Network Security Services (NSS) is a set of libraries for developing
security-enabled client and server applications. This all-in-one package
contains the runtime libraries, development files, and command-line tools.

# No configure
%conf

%install
# no make install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_libdir}
install -d -m 755 %{buildroot}%{_includedir}/nss3
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/pki/nssdb

TARGET_DIR=$(cat dist/latest)
DIST_DIR=dist/$TARGET_DIR

# Use -L to follow symlinks and copy actual files instead of broken symlinks
cp -L $DIST_DIR/bin/* %{buildroot}%{_bindir}/

cp -aL dist/public/nss/*.h %{buildroot}%{_includedir}/nss3/

# Install .so and .chk files from nss/lib only (exclude nspr), following symlinks
find nss/lib -name "*.so" -path "*${TARGET_DIR}*" ! -name "libnspr*" ! -name "libplc*" ! -name "libplds*" -exec sh -c 'cp -L "$1" %{buildroot}%{_libdir}/' _ {} \;
find nss/lib -name "*.chk" -path "*${TARGET_DIR}*" -exec sh -c 'cp -L "$1" %{buildroot}%{_libdir}/' _ {} \;

cd %{buildroot}%{_libdir}
ln -snf libnss3.so libnss3.so.3
ln -snf libnssutil3.so libnssutil3.so.3
ln -snf libsmime3.so libsmime3.so.3
ln -snf libssl3.so libssl3.so.3
ln -snf libsoftokn3.so libsoftokn3.so.3

rm -f %{buildroot}%{_bindir}/{gtests,nss-gtest-all}

# need create pc
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig

cat > %{buildroot}%{_libdir}/pkgconfig/nss-util.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/nss3

Name: NSS-UTIL
Description: Network Security Services Utility Library
Version: 4.37
Requires: nspr
Libs: -L\${libdir} -lnssutil3
Cflags: -I\${includedir}
EOF

cat > %{buildroot}%{_libdir}/pkgconfig/nss.pc << EOF
prefix=%{_prefix}
exec_prefix=%{_exec_prefix}
libdir=%{_libdir}
includedir=%{_includedir}/nss3

Name: NSS
Description: Network Security Services
Version: 3.115
Requires: nspr,nss-util
Libs: -L\${libdir} -lssl3 -lsmime3 -lnss3
Cflags: -I\${includedir}
EOF

# TODO: Add tests
%check

%files
%license nss/COPYING
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/nssdb
%{_libdir}/lib*.so*
%{_libdir}/*.chk
%{_bindir}/*
%{_includedir}/nss3
%{_libdir}/pkgconfig/nss-util.pc
%{_libdir}/pkgconfig/nss.pc

%changelog
%autochangelog

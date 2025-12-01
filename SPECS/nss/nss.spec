# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <1772413353@qq.com>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           nss
Version:        3.115
Release:        %autorelease
Summary:        Network Security Services
License:        MPL-2.0
URL:            https://developer.mozilla.org/en-US/docs/Mozilla/Projects/NSS
#!RemoteAsset
Source:         https://ftp.mozilla.org/pub/security/nss/releases/NSS_3_115_RTM/src/nss-3.115-with-nspr-4.37.tar.gz
BuildSystem:    autotools

BuildOption(build): -C nss
BuildOption(build): nss_build_all
BuildOption(build): BUILD_OPT=1
BuildOption(build): NSS_USE_SYSTEM_SQLITE=1
BuildOption(build): NSS_ENABLE_WERROR=0
BuildOption(build): USE_64=1

BuildRequires:  gcc-c++ make sqlite-devel
BuildRequires:  zlib-devel perl which

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
install -d -m 755 %{buildroot}%{_includedir}/nspr4
install -d -m 755 %{buildroot}%{_libdir}/pkgconfig
install -d -m 755 %{buildroot}%{_sysconfdir}/pki/nssdb

TARGET_DIR=$(cat dist/latest)
DIST_DIR=dist/$TARGET_DIR

cp -a $DIST_DIR/bin/* %{buildroot}%{_bindir}/
cp -a $DIST_DIR/lib/* %{buildroot}%{_libdir}/

cp -aL dist/public/nss/*.h %{buildroot}%{_includedir}/nss3/

cp -aL $DIST_DIR/include/*.h %{buildroot}%{_includedir}/nspr4/

find nss/lib -name "*.so" -path "*${TARGET_DIR}*" -exec install -p -m 755 {} %{buildroot}%{_libdir}/ \;
find nss/lib -name "*.a" -path "*${TARGET_DIR}*" -exec install -p -m 644 {} %{buildroot}%{_libdir}/ \;
find nss/lib -name "*.chk" -path "*${TARGET_DIR}*" -exec install -p -m 644 {} %{buildroot}%{_libdir}/ \;

cd %{buildroot}%{_libdir}
ln -snf libnss3.so libnss3.so.3
ln -snf libnssutil3.so libnssutil3.so.3
ln -snf libsmime3.so libsmime3.so.3
ln -snf libssl3.so libssl3.so.3
ln -snf libsoftokn3.so libsoftokn3.so.3
ln -snf libnspr4.so libnspr4.so.0
ln -snf libplc4.so libplc4.so.0
ln -snf libplds4.so libplds4.so.0

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
Version: 3.94
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
Requires: nspr
Libs: -L\${libdir} -lssl3 -lsmime3 -lnss3
Cflags: -I\${includedir}
EOF

# TODO: Add tests
%check

%files
%license nss/COPYING
%dir %{_sysconfdir}/pki
%dir %{_sysconfdir}/pki/nssdb
%exclude %{_libdir}/libnspr4.so
%exclude %{_libdir}/libplc4.so
%exclude %{_libdir}/libplds4.so
%{_libdir}/lib*.so*
%{_libdir}/*.chk
%{_bindir}/*
%{_includedir}/nss3/
%{_includedir}/nspr4/
%{_libdir}/lib*.a
%{_libdir}/pkgconfig/nss-util.pc
%{_libdir}/pkgconfig/nss.pc

%changelog
%{?autochangelog}

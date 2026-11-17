# SPDX-FileCopyrightText: (C) 2025, 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025, 2026 openRuyi Project Contributors
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           zchunk
Version:        1.5.3
Release:        %autorelease
Summary:        Compressed file format that allows easy deltas
License:        BSD-2-Clause AND MIT
URL:            https://github.com/zchunk/zchunk
#!RemoteAsset:  sha256:832381dafe192109742c141ab90a6bc0a9d7e9926a4bafbdf98f596680da2a95
Source0:        %{url}/archive/%{version}/zchunk-%{version}.tar.gz
# BEGIN openRuyi-test-adapter zchunk sources
Source1:        zchunk-tests
Source2:        zchunk-tests.json
Source3:        zchunk-installed-test
# END openRuyi-test-adapter zchunk sources
BuildSystem:    meson

BuildOption(conf):  -Dwith-openssl=enabled
BuildOption(conf):  -Dwith-zstd=enabled

# BEGIN openRuyi-test-adapter zchunk options
BuildOption(conf):  -Dtests=true
# END openRuyi-test-adapter zchunk options
BuildRequires:  gcc
BuildRequires:  pkgconfig(libzstd)
BuildRequires:  pkgconfig(libcurl)
BuildRequires:  pkgconfig(openssl)
BuildRequires:  meson

%description
zchunk is a compressed file format that splits the file into independent
chunks.  This allows you to only download the differences when downloading a
new version of the file, and also makes zchunk files efficient over rsync.
zchunk files are protected with strong checksums to verify that the file you
downloaded is in fact the file you wanted.

%package        devel
Summary:        Headers for building against zchunk
Requires:       %{name}%{_isa} = %{version}-%{release}

%description    devel
This package contains the headers necessary for building against the zchunk
library, libzck.

# BEGIN openRuyi-test-adapter zchunk subpackage
%package        tests
Summary:        Installed upstream tests for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       openruyi-test-runner >= 0.1.0

%description    tests
Installed upstream test binaries and data for %{name}.
# END openRuyi-test-adapter zchunk subpackage
%prep -a
# Remove bundled sha libraries
rm -rf src/lib/hash/sha*

%install -a
# BEGIN openRuyi-test-adapter zchunk install
install -d %{buildroot}%{_libexecdir}/openruyi-tests/%{name}
binary=$(find . -type f -path '*/test/empty' -print -quit)
test -n "$binary"
install -pm0755 "$binary" %{buildroot}%{_libexecdir}/openruyi-tests/%{name}/empty
install -Dpm0755 %{SOURCE1} %{buildroot}%{_libexecdir}/openruyi-tests/%{name}/run
install -Dpm0644 %{SOURCE2} %{buildroot}%{_datadir}/openruyi-tests/v1/%{name}.json
install -Dpm0755 %{SOURCE3} %{buildroot}%{_libexecdir}/openruyi-tests/%{name}/dispatch
# END openRuyi-test-adapter zchunk install

%files
%doc README.md contrib
%{_bindir}/zck*
%{_bindir}/unzck
%{_mandir}/man1/*.gz
%{_libdir}/libzck.so.*

%files devel
%doc zchunk_format.txt
%{_libdir}/libzck.so
%{_libdir}/pkgconfig/zck.pc
%{_includedir}/zck.h

# BEGIN openRuyi-test-adapter zchunk files
%files tests
%{_libexecdir}/openruyi-tests/%{name}/
%{_datadir}/openruyi-tests/v1/%{name}.json
# END openRuyi-test-adapter zchunk files

%changelog
%autochangelog

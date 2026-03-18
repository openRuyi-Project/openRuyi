# SPDX-FileCopyrightText: (C) 2025 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2025 openRuyi Project Contributors
# SPDX-FileContributor: Jingkun Zheng <zhengjingkun@iscas.ac.cn>
# SPDX-FileContributor: Zheng Junjie <zhengjunjie@iscas.ac.cn>
# SPDX-FileContributor: misaka00251 <liuxin@iscas.ac.cn>
# SPDX-FileContributor: yyjeqhc <jialin.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           tzdata
Version:        2025b
Release:        %autorelease
Summary:        Timezone data
# I'm not sure about this... but I checked from below - 251
# https://data.iana.org/time-zones/tzdb-2025b/LICENSE
License:        CC0-1.0 AND BSD-3-Clause
URL:            https://www.iana.org/time-zones
# VCS: No VCS link available
#!RemoteAsset
Source0:        https://www.iana.org/time-zones/repository/releases/tzdata%{version}.tar.gz
#!RemoteAsset
Source1:        https://www.iana.org/time-zones/repository/releases/tzdata%{version}.tar.gz.asc
#!RemoteAsset
Source2:        https://www.iana.org/time-zones/repository/releases/tzcode%{version}.tar.gz
#!RemoteAsset
Source3:        https://www.iana.org/time-zones/repository/releases/tzcode%{version}.tar.gz.asc
BuildSystem:    autotools

# Also extract %%{SOURCE2}
BuildOption(prep):  -a 2
BuildOption(build):  VERSION=%{version} ZFLAGS="-b fat" DATAFORM=vanguard tzdata.zi
BuildOption(check):  CC=%__cc

BuildRequires:  make
BuildRequires:  perl
BuildRequires:  glibc-locale

%description
This package contains data files with rules for various timezones around
the world.

%conf
# No configure

%build -p
# We need zic before compiling tzdata
%make_build TZDIR=%{_datadir}/zoneinfo CC=%__cc CFLAGS="%{optflags} -DHAVE_GETTEXT=1 -DTZDEFAULT='\"%{_sysconfdir}/localtime\"' -DTM_GMTOFF=tm_gmtoff -DTM_ZONE=tm_zone -Dlint" AWK=%__awk KSHELL=%_buildshell

%build -a
FILES="africa antarctica asia australasia europe northamerica southamerica
       etcetera backward factory"
mkdir zoneinfo/{,posix,right}
./zic -b fat -y ./yearistype -d zoneinfo -L /dev/null $FILES
./zic -b fat -y ./yearistype -d zoneinfo/posix -L /dev/null $FILES
./zic -b fat -y ./yearistype -d zoneinfo/right -L leapseconds $FILES

%install
# We control the full install
rm -fr $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}
cp -prd zoneinfo $RPM_BUILD_ROOT%{_datadir}
install -p -m 644 zone.tab zone1970.tab iso3166.tab leap-seconds.list leapseconds tzdata.zi $RPM_BUILD_ROOT%{_datadir}/zoneinfo

install -D -m 755 tzselect %{buildroot}%{_bindir}/tzselect
install -D -m 755 zdump    %{buildroot}%{_bindir}/zdump
install -D -m 755 zic      %{buildroot}%{_bindir}/zic

# Disable checks for now
%check

%files
%license LICENSE
%doc README
%doc theory.html
%doc tz-link.html
%doc tz-art.html
%{_datadir}/zoneinfo
%{_bindir}/zdump
%{_bindir}/zic
%{_bindir}/tzselect

%changelog
%{?autochangelog}

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Xuhai Chang <xuhai.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

Name:           date
Version:        3.0.4
Release:        %autorelease
Summary:        Date and time library based on the C++11/14/17 <chrono> header
License:        MIT
URL:            https://github.com/HowardHinnant/date
#!RemoteAsset
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
BuildSystem:    cmake

# add pkg-config support to make the package compatible with meson
# https://github.com/HowardHinnant/date/pull/538
Patch0:         0001-output-date-pc-for-pkg-config.patch
# Adjust default value of USE_OS_TZDB macro to match build.
Patch1:         0002-date-macro.patch

BuildOption(conf):  -DBUILD_TZ_LIB=ON
BuildOption(conf):  -DUSE_SYSTEM_TZ_DB=ON
BuildOption(conf):  -DENABLE_DATE_TESTING=ON

BuildRequires:  cmake
BuildRequires:  gcc-c++
# for %check
BuildRequires:  tzdata

%description
This is actually several separate C++11/C++14/C++17 libraries:
 - "date.h" is a header-only library which builds upon <chrono>.
   It adds some new duration types, and new time_point types. It
   also adds "field" types such as year_month_day which is a
   struct {year, month, day}. And it provides convenient means
   to convert between the "field" types and the time_point types.
 - "tz.h" / "tz.cpp" are a timezone library built on top of the
   "date.h" library. This timezone library is a complete parser
   of the IANA timezone database. It provides for an easy way to
   access all of the data in this database, using the types from
   "date.h" and <chrono>. The IANA database also includes data
   on leap seconds, and this library provides utilities to compute
   with that information as well.
Slightly modified versions of "date.h" and "tz.h" were voted into
the C++20 standard.

%package        devel
Summary:        Date and time library based on the C++11/14/17 <chrono> header
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
%{summary}

%prep -a
# fails due to missing timezone configuration
rm -f test/tz_test/zoned_time_deduction.pass.cpp
# one more test that depends on localtime. we don't even install this header
rm -rf test/solar_hijri_test/

%check
export CTEST_OUTPUT_ON_FAILURE=ON
%{cmake_build} -t testit

%files
%license LICENSE.txt
%{_libdir}/libdate-tz.so.*

%files devel
%license LICENSE.txt
%doc README.md
%{_includedir}/%{name}/
%{_libdir}/libdate-tz.so
%{_libdir}/cmake/%{name}/
%{_libdir}/pkgconfig/%{name}.pc

%changelog
%autochangelog

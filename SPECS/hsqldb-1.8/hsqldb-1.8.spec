# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global lo_version 26.8.2.2

Name:           hsqldb-1.8
Version:        1.8.0.10
Release:        %autorelease
Summary:        HyperSQL 1.8 embedded database engine
License:        BSD-3-Clause
URL:            https://hsqldb.org/
VCS:            svn:https://svn.code.sf.net/p/hsqldb/svn/
#!RemoteAsset:  sha256:d30b13f4ba2e3b6a2d4f020c0dee0a9fb9fc6fbcc2d561f36b78da4bf3802370
Source0:        https://downloads.sourceforge.net/project/hsqldb/hsqldb/hsqldb_1_8_0/hsqldb_1_8_0_10.zip
# Upstream LibreOffice changes for its embedded HSQLDB driver, applied in upstream order.
# https://github.com/LibreOffice/core/blob/libreoffice-26.8.2.2/external/hsqldb/UnpackedTarball_hsqldb.mk
#!RemoteAsset:  sha256:51bb07050975c377d5a12c6dac70be5585cad1c8d1591c2ae04f28935973dab8
Source1:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/i96823.patch#/2000-i96823.patch
#!RemoteAsset:  sha256:075f55c1bef6a3f9080ae36c7934e3aa3ddc95a78605a061e170560c4a7a53d8
Source2:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/i97032.patch#/2001-i97032.patch
#!RemoteAsset:  sha256:582186e440580830327e1383753dee98bc0f8c12ee2c3a10b08a7faa38025ff8
Source3:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/i103528.patch#/2002-i103528.patch
#!RemoteAsset:  sha256:d89e14111aeb6ea96d29a3804ac00c6266262a21166510b99bf34234800b0dd5
Source4:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/i104901.patch#/2003-i104901.patch
#!RemoteAsset:  sha256:829854ca1704909e407468bdf1ea40548706d9b838ed84fae696a9921c4d8f85
Source5:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/fdo36824.patch#/2004-fdo36824.patch
#!RemoteAsset:  sha256:1c4c9950cc181702c327cb595edf368c1da32e023e5228dc2405f5249270ea63
Source6:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/limit_as_table_alias.patch#/2005-limit_as_table_alias.patch
#!RemoteAsset:  sha256:6a53c3d2f25686382e880d40d18db658a14260fe626c2070adc011081593e2c3
Source7:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/hsqldb-runFinalizersOnExit.patch#/2006-hsqldb-runFinalizersOnExit.patch
#!RemoteAsset:  sha256:c486fddfa69f290b7d59fdfe553d15c09eae51bae6c29e875500abf534ad49f1
Source8:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/jdbc-4.1.patch#/2007-jdbc-4.1.patch
#!RemoteAsset:  sha256:9885cbcd657fd4496af1526073678970827242dd9d954debdf4fbd80f6b3e128
Source9:        https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/multipleResultSets.patch#/2008-multipleResultSets.patch
#!RemoteAsset:  sha256:fbdab06005a6d5e99c8a412a0539a926161a9782358782354caf0e2f5a9727cb
Source10:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/disable-dump-script.patch#/2009-disable-dump-script.patch
#!RemoteAsset:  sha256:c655b8c5ce5a426bb09d66c75abb005038db9507192fc00206915123eacee3e1
Source11:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/abstract.patch#/2010-abstract.patch
#!RemoteAsset:  sha256:b49b3ddec30ea28fce481dd977173fe31d597e38a6861d4ccb9271c727b494e4
Source12:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/applet.patch.0#/2011-applet.patch
#!RemoteAsset:  sha256:b099b7463ff89b3828d610b9658837bd1435d9a22e687146fa43b4a08f839d18
Source13:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/lockfile.patch.1#/2012-lockfile.patch
#!RemoteAsset:  sha256:2604410129b0fe46bf7699e970215d8fca9e2e47f143d7e24c4ece7fde2019ea
Source14:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/allow-full-path-system-property.patch.1#/2013-allow-full-path-system-property.patch
#!RemoteAsset:  sha256:e66f09a24367de1e6f64aec3d5e2efe3edc60b9a98c8d8e8f8c8b3655d8f796e
Source15:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/stored-text-table.patch.1#/2014-stored-text-table.patch
#!RemoteAsset:  sha256:6efe8abebaac08d23f6186c31b74c92978ccbc51ac113dca34e12ee3de8a4446
Source16:       https://raw.githubusercontent.com/LibreOffice/core/libreoffice-%{lo_version}/external/hsqldb/patches/method-class-names-default.patch#/2015-method-class-names-default.patch
BuildArch:      noarch

BuildRequires:  ant
BuildRequires:  junit4
BuildRequires:  java-25-openjdk-devel
BuildRequires:  javax-servlet-api
BuildRequires:  patch
BuildRequires:  unzip
Requires:       java-25-openjdk-headless

%patchlist
%{SOURCE1}
%{SOURCE2}
%{SOURCE3}
%{SOURCE4}
%{SOURCE5}
%{SOURCE6}
%{SOURCE7}
%{SOURCE8}
%{SOURCE9}
%{SOURCE10}
%{SOURCE11}
%{SOURCE12}
%{SOURCE13}
%{SOURCE14}
%{SOURCE15}
%{SOURCE16}

# Downstream build-environment adaptation of the upstream HTTP savepoint test.
# https://sourceforge.net/projects/hsqldb/files/hsqldb/hsqldb_1_8_0_10/
2016-use-unprivileged-http-test-port.patch

%description
HyperSQL 1.8 is a Java SQL database engine for legacy embedded databases.
LibreOffice Base uses this version to open and edit existing HSQLDB files.

%prep
%autosetup -N -n hsqldb
# Normalize the three CRLF inputs listed in LibreOffice's UnpackedTarball recipe.
sed -i 's/\r$//' build/build.xml src/org/hsqldb/Library.java src/org/hsqldb/persist/HsqlDatabaseProperties.java
rm -f lib/hsqldb.jar lib/servlet.jar
# Upstream patch paths use different strip levels; apply each contiguous group in order.
%autopatch -p2 -m0 -M10
%autopatch -p0 -m11 -M11
%autopatch -p1 -m12 -M14
%autopatch -p2 -m15 -M15
%autopatch -p1 -m16 -M16
ln -s %{_datadir}/java/javax-servlet-api.jar lib/servlet.jar

%build
ant -nouserlib -f build/build.xml -Dbuild.label=%{version} \
    -Dant.build.javac.source=8 -Dant.build.javac.target=8 -Dnoswing=true jar

%install
install -Dpm644 lib/hsqldb.jar %{buildroot}%{_datadir}/java/hsqldb1.8/hsqldb.jar

%check
# Run the self-contained JDBC suites listed by upstream AllTests.
# TestGroupByHaving, TestSubselect and TestSqlPersistent depend on TestSelf,
# whose StringComparator helper is absent from this release. The persistent
# suite additionally hardcodes the unwritable /hsql/test database directory.
mkdir classes-test
suites="org.hsqldb.test.TestBatchExecution
org.hsqldb.test.TestBug778213
org.hsqldb.test.TestBug785429
org.hsqldb.test.TestBug808460
org.hsqldb.test.TestDatabaseMetaData
org.hsqldb.test.TestDateTime
org.hsqldb.test.TestJDBCSavepoints
org.hsqldb.test.TestINPredicateParameterizationAndCorrelation
org.hsqldb.test.TestLikePredicateOptimizations
org.hsqldb.test.TestSql
org.hsqldb.test.TestTimestamp
org.hsqldb.test.TestViewAsterisks"
for suite in $suites; do printf 'src/%s.java\n' "$(echo "$suite" | tr . /)"; done > test.sources
javac --release 8 -encoding UTF-8 -cp lib/hsqldb.jar:%{_datadir}/java/junit4.jar -sourcepath src -d classes-test @test.sources
java -cp classes-test:lib/hsqldb.jar:%{_datadir}/java/junit4.jar org.junit.runner.JUnitCore $suites

%files
%license doc/hsqldb_lic.txt doc/hypersonic_lic.txt
%{_datadir}/java/hsqldb1.8/

%changelog
%autochangelog

# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: Li Guan <guanli.oerv@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global commit 66a8ae7fe741d03608b7454f994269b5c4531090

Name:           ehcache
Version:        1.5.0
Release:        %autorelease
Summary:        Ehcache memory and disk cache for Java
License:        Apache-2.0
URL:            https://www.ehcache.org/
VCS:            git:https://github.com/ehcache/ehcache2.git
#!RemoteAsset:  sha256:5139515731eb0525fc36a63baab202812139c861b640dd71a319174bbb498d0b
Source0:        https://github.com/ehcache/ehcache2/archive/%{commit}.tar.gz#/%{name}-%{version}.tar.gz
#!RemoteAsset:  sha256:cfc7749b96f63bd31c3c42b5c471bf756814053e847c10f3eb003417bc523d30
Source1:        https://www.apache.org/licenses/LICENSE-2.0.txt
BuildArch:      noarch

BuildRequires:  java-25-openjdk-devel
BuildRequires:  junit4
BuildRequires:  backport-util-concurrent
BuildRequires:  commons-collections-3
BuildRequires:  jsr107cache
BuildRequires:  slf4j-jcl
BuildRequires:  slf4j-jdk14
Requires:       backport-util-concurrent
Requires:       commons-collections-3
Requires:       jsr107cache
Requires:       slf4j-jcl
Requires:       slf4j-jdk14

%description
Ehcache caches Java objects in memory or on disk and supplies the cache
manager, loaders and stores used by reporting applications.

%prep
%autosetup -n ehcache2-%{commit}
cp -p %{SOURCE1} LICENSE-2.0.txt

%build
mkdir classes
# Hibernate, servlet and JGroups adapters require external containers or a cluster.
# The resource loader uses the standalone cache, JCache interfaces and stores.
find core/src/main/java/net -name '*.java' ! -path '*/hibernate/*' ! -path '*/constructs/web/*' ! -path '*/distribution/jgroups/*' | sort > sources.list
cp=%{_datadir}/java/backport-util-concurrent.jar:%{_datadir}/java/jsr107cache.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar
javac --release 8 -encoding UTF-8 -cp "$cp" -d classes @sources.list
cp -a core/src/main/resources/. classes/
printf 'Class-Path: backport-util-concurrent.jar jsr107cache.jar commons-collections3.jar jcl-over-slf4j.jar slf4j-jdk14.jar\n' > manifest.mf
jar --create --file ehcache.jar --manifest manifest.mf -C classes .

%install
install -Dpm644 ehcache.jar %{buildroot}%{_datadir}/java/ehcache.jar

%check
# Run upstream standalone cache, element, disk-store and statistics tests.
# Web, Hibernate and clustered integration suites exercise adapters omitted from this build.
mkdir classes-test
cp=ehcache.jar:%{_datadir}/java/backport-util-concurrent.jar:%{_datadir}/java/jsr107cache.jar:%{_datadir}/java/commons-collections3.jar:%{_datadir}/java/jcl-over-slf4j.jar:%{_datadir}/java/slf4j-jdk14.jar:%{_datadir}/java/junit4.jar
find core/src/test/java/net/sf/ehcache -maxdepth 1 -name '*.java' | sort > test.sources
# The XML fixtures instantiate these upstream test factories by reflection.
printf '%s\n' core/src/test/java/net/sf/ehcache/event/CountingCacheEventListenerFactory.java core/src/test/java/net/sf/ehcache/event/NullCacheEventListenerFactory.java core/src/test/java/net/sf/ehcache/event/TestCacheManagerEventListenerFactory.java core/src/test/java/net/sf/ehcache/exceptionhandler/CountingExceptionHandlerFactory.java core/src/test/java/net/sf/ehcache/extension/TestCacheExtensionFactory.java core/src/test/java/net/sf/ehcache/loader/ComponentALoader.java core/src/test/java/net/sf/ehcache/loader/ComponentBLoader.java core/src/test/java/net/sf/ehcache/loader/CountingCacheLoaderFactory.java >> test.sources
javac --release 8 -encoding UTF-8 -cp "$cp" -sourcepath core/src/test/java -d classes-test @test.sources
cp -rp core/src/test/resources/. classes-test/
# Match the upstream module working directory. Isolate test methods because
# cache-manager shutdown leaves asynchronous RMI and disk-store worker threads.
# DiskStoreTest expects a 64 MiB heap; allow extra spool time through upstream's setting.
cp="$PWD/classes-test:$PWD/$cp"
cd core
for suite in CacheExceptionTest CacheManagerTest CacheTest DiskStoreTest ElementTest StatusTest; do
    methods=$(sed -n 's/.*public void \(test[A-Za-z0-9_]*\)(.*/\1/p' "src/test/java/net/sf/ehcache/$suite.java")
    for method in $methods; do
        java -Xmx64m -Djava.awt.headless=true -Dnet.sf.ehcache.speedAdjustmentFactor=4 -cp "$cp" junit.textui.TestRunner -m "net.sf.ehcache.$suite.$method" || exit 1
    done
done
# testAverageGetTime assumes reads take at least 0.05 ms, which is not portable to
# current processors. Run every other upstream StatisticsTest method unchanged.
for method in testStatistics testStatisticsFromStatisticsObject testClearStatistics testCacheStatisticsDegradesElegantlyWhenCacheDisposed testSerialization testIntOverflow testEvictionStatistics; do
    java -Xmx64m -Djava.awt.headless=true -cp "$cp" junit.textui.TestRunner -m "net.sf.ehcache.StatisticsTest.$method" || exit 1
done

%files
%license core/LICENSE.txt LICENSE-2.0.txt
%{_datadir}/java/ehcache.jar

%changelog
%autochangelog

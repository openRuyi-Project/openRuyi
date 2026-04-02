# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
# SPDX-FileContributor: purofle <yuguo.or@isrc.iscas.ac.cn>
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-data
%global full_version 0.3.2
%global pkgname objc2-core-data-0.3

Name:           rust-objc2-core-data-0.3
Version:        0.3.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-data"
License:        Zlib OR Apache-2.0 OR MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:0b402a653efbb5e82ce4df10683b6b28027616a2715e90009947d50b8dd298fa
Source:         https://crates.io/api/v1/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.6/std) >= 0.6.4
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Provides:       crate(%{pkgname})
Provides:       crate(%{pkgname}/coredatadefines)
Provides:       crate(%{pkgname}/alloc)
Provides:       crate(%{pkgname}/gnustep-1-7)
Provides:       crate(%{pkgname}/gnustep-1-8)
Provides:       crate(%{pkgname}/gnustep-1-9)
Provides:       crate(%{pkgname}/gnustep-2-0)
Provides:       crate(%{pkgname}/gnustep-2-1)
Provides:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/unstable-darwin-objc)

%description
Source code for takopackized Rust crate "objc2-core-data"

%package     -n %{name}+cloudkit
Summary:        Bindings to the CoreData framework - feature "CloudKit"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/cloudkit)

%description -n %{name}+cloudkit
This metapackage enables feature "CloudKit" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+coredataerrors
Summary:        Bindings to the CoreData framework - feature "CoreDataErrors" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/coredataerrors)
Provides:       crate(%{pkgname}/nsmigrationstage)
Provides:       crate(%{pkgname}/nspersistentcloudkitcontaineroptions)

%description -n %{name}+coredataerrors
This metapackage enables feature "CoreDataErrors" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSMigrationStage", and "NSPersistentCloudKitContainerOptions" features.

%package     -n %{name}+nsatomicstore
Summary:        Bindings to the CoreData framework - feature "NSAtomicStore"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsatomicstore)

%description -n %{name}+nsatomicstore
This metapackage enables feature "NSAtomicStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsatomicstorecachenode
Summary:        Bindings to the CoreData framework - feature "NSAtomicStoreCacheNode" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsatomicstorecachenode)
Provides:       crate(%{pkgname}/nsincrementalstorenode)

%description -n %{name}+nsatomicstorecachenode
This metapackage enables feature "NSAtomicStoreCacheNode" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSIncrementalStoreNode" feature.

%package     -n %{name}+nsattributedescription
Summary:        Bindings to the CoreData framework - feature "NSAttributeDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsattributedescription)

%description -n %{name}+nsattributedescription
This metapackage enables feature "NSAttributeDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbatchdeleterequest
Summary:        Bindings to the CoreData framework - feature "NSBatchDeleteRequest" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsbatchdeleterequest)
Provides:       crate(%{pkgname}/nscompositeattributedescription)
Provides:       crate(%{pkgname}/nspersistentstorerequest)

%description -n %{name}+nsbatchdeleterequest
This metapackage enables feature "NSBatchDeleteRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSCompositeAttributeDescription", and "NSPersistentStoreRequest" features.

%package     -n %{name}+nsbatchinsertrequest
Summary:        Bindings to the CoreData framework - feature "NSBatchInsertRequest"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsbatchinsertrequest)

%description -n %{name}+nsbatchinsertrequest
This metapackage enables feature "NSBatchInsertRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbatchupdaterequest
Summary:        Bindings to the CoreData framework - feature "NSBatchUpdateRequest"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsbatchupdaterequest)

%description -n %{name}+nsbatchupdaterequest
This metapackage enables feature "NSBatchUpdateRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscoredatacorespotlightdelegate
Summary:        Bindings to the CoreData framework - feature "NSCoreDataCoreSpotlightDelegate"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nscoredatacorespotlightdelegate)

%description -n %{name}+nscoredatacorespotlightdelegate
This metapackage enables feature "NSCoreDataCoreSpotlightDelegate" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscustommigrationstage
Summary:        Bindings to the CoreData framework - feature "NSCustomMigrationStage"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Provides:       crate(%{pkgname}/nscustommigrationstage)

%description -n %{name}+nscustommigrationstage
This metapackage enables feature "NSCustomMigrationStage" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsderivedattributedescription
Summary:        Bindings to the CoreData framework - feature "NSDerivedAttributeDescription" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsexpression) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsderivedattributedescription)
Provides:       crate(%{pkgname}/nsexpressiondescription)

%description -n %{name}+nsderivedattributedescription
This metapackage enables feature "NSDerivedAttributeDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSExpressionDescription" feature.

%package     -n %{name}+nsentitydescription
Summary:        Bindings to the CoreData framework - feature "NSEntityDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsenumerator) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsexpression) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsentitydescription)

%description -n %{name}+nsentitydescription
This metapackage enables feature "NSEntityDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsentitymapping
Summary:        Bindings to the CoreData framework - feature "NSEntityMapping"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsexpression) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsentitymapping)

%description -n %{name}+nsentitymapping
This metapackage enables feature "NSEntityMapping" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsentitymigrationpolicy
Summary:        Bindings to the CoreData framework - feature "NSEntityMigrationPolicy"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsentitymigrationpolicy)

%description -n %{name}+nsentitymigrationpolicy
This metapackage enables feature "NSEntityMigrationPolicy" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchindexdescription
Summary:        Bindings to the CoreData framework - feature "NSFetchIndexDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchindexdescription)

%description -n %{name}+nsfetchindexdescription
This metapackage enables feature "NSFetchIndexDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchindexelementdescription
Summary:        Bindings to the CoreData framework - feature "NSFetchIndexElementDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchindexelementdescription)

%description -n %{name}+nsfetchindexelementdescription
This metapackage enables feature "NSFetchIndexElementDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchrequest
Summary:        Bindings to the CoreData framework - feature "NSFetchRequest"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nssortdescriptor) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchrequest)

%description -n %{name}+nsfetchrequest
This metapackage enables feature "NSFetchRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchrequestexpression
Summary:        Bindings to the CoreData framework - feature "NSFetchRequestExpression"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nscoder) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsexpression) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchrequestexpression)

%description -n %{name}+nsfetchrequestexpression
This metapackage enables feature "NSFetchRequestExpression" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchedpropertydescription
Summary:        Bindings to the CoreData framework - feature "NSFetchedPropertyDescription" and 2 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchedpropertydescription)
Provides:       crate(%{pkgname}/nspersistenthistorytoken)
Provides:       crate(%{pkgname}/nsquerygenerationtoken)

%description -n %{name}+nsfetchedpropertydescription
This metapackage enables feature "NSFetchedPropertyDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPersistentHistoryToken", and "NSQueryGenerationToken" features.

%package     -n %{name}+nsfetchedresultscontroller
Summary:        Bindings to the CoreData framework - feature "NSFetchedResultsController"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/nsfetchrequest)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsindexpath) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsorderedcollectiondifference) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsfetchedresultscontroller)

%description -n %{name}+nsfetchedresultscontroller
This metapackage enables feature "NSFetchedResultsController" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsincrementalstore
Summary:        Bindings to the CoreData framework - feature "NSIncrementalStore" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsincrementalstore)
Provides:       crate(%{pkgname}/nsmigrationmanager)

%description -n %{name}+nsincrementalstore
This metapackage enables feature "NSIncrementalStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSMigrationManager" feature.

%package     -n %{name}+nslightweightmigrationstage
Summary:        Bindings to the CoreData framework - feature "NSLightweightMigrationStage"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nslightweightmigrationstage)

%description -n %{name}+nslightweightmigrationstage
This metapackage enables feature "NSLightweightMigrationStage" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobject
Summary:        Bindings to the CoreData framework - feature "NSManagedObject"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nskeyvalueobserving) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsmanagedobject)

%description -n %{name}+nsmanagedobject
This metapackage enables feature "NSManagedObject" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectcontext
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectContext"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslock) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsundomanager) >= 0.3.2
Provides:       crate(%{pkgname}/nsmanagedobjectcontext)

%description -n %{name}+nsmanagedobjectcontext
This metapackage enables feature "NSManagedObjectContext" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectid
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectID"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsmanagedobjectid)

%description -n %{name}+nsmanagedobjectid
This metapackage enables feature "NSManagedObjectID" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectmodel
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectModel"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsenumerator) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsmanagedobjectmodel)

%description -n %{name}+nsmanagedobjectmodel
This metapackage enables feature "NSManagedObjectModel" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectmodelreference
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectModelReference"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsmanagedobjectmodelreference)

%description -n %{name}+nsmanagedobjectmodelreference
This metapackage enables feature "NSManagedObjectModelReference" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmappingmodel
Summary:        Bindings to the CoreData framework - feature "NSMappingModel"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsbundle) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nsmappingmodel)

%description -n %{name}+nsmappingmodel
This metapackage enables feature "NSMappingModel" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmergepolicy
Summary:        Bindings to the CoreData framework - feature "NSMergePolicy"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nsmergepolicy)

%description -n %{name}+nsmergepolicy
This metapackage enables feature "NSMergePolicy" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainer
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainer"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainer)

%description -n %{name}+nspersistentcloudkitcontainer
This metapackage enables feature "NSPersistentCloudKitContainer" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainerevent
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainerEvent"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsuuid) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainerevent)

%description -n %{name}+nspersistentcloudkitcontainerevent
This metapackage enables feature "NSPersistentCloudKitContainerEvent" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainereventrequest
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainerEventRequest" and 1 more
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainereventrequest)
Provides:       crate(%{pkgname}/nspersistenthistorychangerequest)

%description -n %{name}+nspersistentcloudkitcontainereventrequest
This metapackage enables feature "NSPersistentCloudKitContainerEventRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPersistentHistoryChangeRequest" feature.

%package     -n %{name}+nspersistentcontainer
Summary:        Bindings to the CoreData framework - feature "NSPersistentContainer"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentcontainer)

%description -n %{name}+nspersistentcontainer
This metapackage enables feature "NSPersistentContainer" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistenthistorychange
Summary:        Bindings to the CoreData framework - feature "NSPersistentHistoryChange"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistenthistorychange)

%description -n %{name}+nspersistenthistorychange
This metapackage enables feature "NSPersistentHistoryChange" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistenthistorytransaction
Summary:        Bindings to the CoreData framework - feature "NSPersistentHistoryTransaction"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsnotification) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistenthistorytransaction)

%description -n %{name}+nspersistenthistorytransaction
This metapackage enables feature "NSPersistentHistoryTransaction" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstore
Summary:        Bindings to the CoreData framework - feature "NSPersistentStore"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentstore)

%description -n %{name}+nspersistentstore
This metapackage enables feature "NSPersistentStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstorecoordinator
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreCoordinator"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nslock) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsvalue) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentstorecoordinator)

%description -n %{name}+nspersistentstorecoordinator
This metapackage enables feature "NSPersistentStoreCoordinator" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstoredescription
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsurl) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentstoredescription)

%description -n %{name}+nspersistentstoredescription
This metapackage enables feature "NSPersistentStoreDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstoreresult
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreResult"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/nsfetchrequest)
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nserror) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsprogress) >= 0.3.2
Provides:       crate(%{pkgname}/nspersistentstoreresult)

%description -n %{name}+nspersistentstoreresult
This metapackage enables feature "NSPersistentStoreResult" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspropertydescription
Summary:        Bindings to the CoreData framework - feature "NSPropertyDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nspredicate) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nspropertydescription)

%description -n %{name}+nspropertydescription
This metapackage enables feature "NSPropertyDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspropertymapping
Summary:        Bindings to the CoreData framework - feature "NSPropertyMapping"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdictionary) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsexpression) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsstring) >= 0.3.2
Provides:       crate(%{pkgname}/nspropertymapping)

%description -n %{name}+nspropertymapping
This metapackage enables feature "NSPropertyMapping" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsrelationshipdescription
Summary:        Bindings to the CoreData framework - feature "NSRelationshipDescription"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsdata) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Provides:       crate(%{pkgname}/nsrelationshipdescription)

%description -n %{name}+nsrelationshipdescription
This metapackage enables feature "NSRelationshipDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nssavechangesrequest
Summary:        Bindings to the CoreData framework - feature "NSSaveChangesRequest"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsobject) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsset) >= 0.3.2
Provides:       crate(%{pkgname}/nssavechangesrequest)

%description -n %{name}+nssavechangesrequest
This metapackage enables feature "NSSaveChangesRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsstagedmigrationmanager
Summary:        Bindings to the CoreData framework - feature "NSStagedMigrationManager"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-foundation-0.3/alloc) >= 0.3.2
Requires:       crate(objc2-foundation-0.3/nsarray) >= 0.3.2
Provides:       crate(%{pkgname}/nsstagedmigrationmanager)

%description -n %{name}+nsstagedmigrationmanager
This metapackage enables feature "NSStagedMigrationManager" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreData framework - feature "bitflags"
Requires:       crate(%{pkgname})
Requires:       crate(bitflags-2.0/std) >= 2.5.0
Provides:       crate(%{pkgname}/bitflags)

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreData framework - feature "block2"
Requires:       crate(%{pkgname})
Requires:       crate(block2-0.6/alloc) >= 0.6.1
Provides:       crate(%{pkgname}/block2)

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+default
Summary:        Bindings to the CoreData framework - feature "default"
Requires:       crate(%{pkgname})
Requires:       crate(%{pkgname}/bitflags)
Requires:       crate(%{pkgname}/block2)
Requires:       crate(%{pkgname}/cloudkit)
Requires:       crate(%{pkgname}/coredatadefines)
Requires:       crate(%{pkgname}/coredataerrors)
Requires:       crate(%{pkgname}/nsatomicstore)
Requires:       crate(%{pkgname}/nsatomicstorecachenode)
Requires:       crate(%{pkgname}/nsattributedescription)
Requires:       crate(%{pkgname}/nsbatchdeleterequest)
Requires:       crate(%{pkgname}/nsbatchinsertrequest)
Requires:       crate(%{pkgname}/nsbatchupdaterequest)
Requires:       crate(%{pkgname}/nscompositeattributedescription)
Requires:       crate(%{pkgname}/nscoredatacorespotlightdelegate)
Requires:       crate(%{pkgname}/nscustommigrationstage)
Requires:       crate(%{pkgname}/nsderivedattributedescription)
Requires:       crate(%{pkgname}/nsentitydescription)
Requires:       crate(%{pkgname}/nsentitymapping)
Requires:       crate(%{pkgname}/nsentitymigrationpolicy)
Requires:       crate(%{pkgname}/nsexpressiondescription)
Requires:       crate(%{pkgname}/nsfetchedpropertydescription)
Requires:       crate(%{pkgname}/nsfetchedresultscontroller)
Requires:       crate(%{pkgname}/nsfetchindexdescription)
Requires:       crate(%{pkgname}/nsfetchindexelementdescription)
Requires:       crate(%{pkgname}/nsfetchrequest)
Requires:       crate(%{pkgname}/nsfetchrequestexpression)
Requires:       crate(%{pkgname}/nsincrementalstore)
Requires:       crate(%{pkgname}/nsincrementalstorenode)
Requires:       crate(%{pkgname}/nslightweightmigrationstage)
Requires:       crate(%{pkgname}/nsmanagedobject)
Requires:       crate(%{pkgname}/nsmanagedobjectcontext)
Requires:       crate(%{pkgname}/nsmanagedobjectid)
Requires:       crate(%{pkgname}/nsmanagedobjectmodel)
Requires:       crate(%{pkgname}/nsmanagedobjectmodelreference)
Requires:       crate(%{pkgname}/nsmappingmodel)
Requires:       crate(%{pkgname}/nsmergepolicy)
Requires:       crate(%{pkgname}/nsmigrationmanager)
Requires:       crate(%{pkgname}/nsmigrationstage)
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainer)
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainerevent)
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainereventrequest)
Requires:       crate(%{pkgname}/nspersistentcloudkitcontaineroptions)
Requires:       crate(%{pkgname}/nspersistentcontainer)
Requires:       crate(%{pkgname}/nspersistenthistorychange)
Requires:       crate(%{pkgname}/nspersistenthistorychangerequest)
Requires:       crate(%{pkgname}/nspersistenthistorytoken)
Requires:       crate(%{pkgname}/nspersistenthistorytransaction)
Requires:       crate(%{pkgname}/nspersistentstore)
Requires:       crate(%{pkgname}/nspersistentstorecoordinator)
Requires:       crate(%{pkgname}/nspersistentstoredescription)
Requires:       crate(%{pkgname}/nspersistentstorerequest)
Requires:       crate(%{pkgname}/nspersistentstoreresult)
Requires:       crate(%{pkgname}/nspropertydescription)
Requires:       crate(%{pkgname}/nspropertymapping)
Requires:       crate(%{pkgname}/nsquerygenerationtoken)
Requires:       crate(%{pkgname}/nsrelationshipdescription)
Requires:       crate(%{pkgname}/nssavechangesrequest)
Requires:       crate(%{pkgname}/nsstagedmigrationmanager)
Requires:       crate(%{pkgname}/objc2-cloud-kit)
Requires:       crate(%{pkgname}/std)
Provides:       crate(%{pkgname}/default)

%description -n %{name}+default
This metapackage enables feature "default" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-cloud-kit
Summary:        Bindings to the CoreData framework - feature "objc2-cloud-kit"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-cloud-kit-0.3/ckcontainer) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckdatabase) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckrecord) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckrecordid) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckrecordzoneid) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckshare) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/cksharemetadata) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckshareparticipant) >= 0.3.2
Requires:       crate(objc2-cloud-kit-0.3/ckuseridentitylookupinfo) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-cloud-kit)

%description -n %{name}+objc2-cloud-kit
This metapackage enables feature "objc2-cloud-kit" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+objc2-core-spotlight
Summary:        Bindings to the CoreData framework - feature "objc2-core-spotlight"
Requires:       crate(%{pkgname})
Requires:       crate(objc2-core-spotlight-0.3/cssearchableindex) >= 0.3.2
Requires:       crate(objc2-core-spotlight-0.3/cssearchableitemattributeset) >= 0.3.2
Provides:       crate(%{pkgname}/objc2-core-spotlight)

%description -n %{name}+objc2-core-spotlight
This metapackage enables feature "objc2-core-spotlight" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

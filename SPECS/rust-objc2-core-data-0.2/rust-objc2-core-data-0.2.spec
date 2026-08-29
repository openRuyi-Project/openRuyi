# SPDX-FileCopyrightText: (C) 2026 Institute of Software, Chinese Academy of Sciences (ISCAS)
# SPDX-FileCopyrightText: (C) 2026 openRuyi Project Contributors
#
# SPDX-License-Identifier: MulanPSL-2.0

%global crate_name objc2-core-data
%global full_version 0.2.2
%global pkgname objc2-core-data-0.2

Name:           rust-objc2-core-data-0.2
Version:        0.2.2
Release:        %autorelease
Summary:        Rust crate "objc2-core-data"
License:        MIT
URL:            https://github.com/madsmtm/objc2
#!RemoteAsset:  sha256:617fbf49e071c178c0b24c080767db52958f716d9eabdf0890523aeae54773ef
Source:         https://static.crates.io/crates/%{crate_name}/%{full_version}/download#/%{name}-%{version}.tar.gz
BuildArch:      noarch
BuildSystem:    rustcrates

BuildRequires:  rust-rpm-macros

Requires:       crate(objc2-0.5) >= 0.5.2
Requires:       crate(objc2-foundation-0.2) >= 0.2.2
Provides:       crate(%{pkgname}) = %{version}
Provides:       crate(%{pkgname}/apple) = %{version}
Provides:       crate(%{pkgname}/coredatadefines) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-7) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-8) = %{version}
Provides:       crate(%{pkgname}/gnustep-1-9) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-0) = %{version}
Provides:       crate(%{pkgname}/gnustep-2-1) = %{version}

%description
Source code for takopackized Rust crate "objc2-core-data"

%package     -n %{name}+coredataerrors
Summary:        Bindings to the CoreData framework - feature "CoreDataErrors" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/coredataerrors) = %{version}
Provides:       crate(%{pkgname}/nsmigrationstage) = %{version}
Provides:       crate(%{pkgname}/nspersistentcloudkitcontaineroptions) = %{version}

%description -n %{name}+coredataerrors
This metapackage enables feature "CoreDataErrors" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSMigrationStage", and "NSPersistentCloudKitContainerOptions" features.

%package     -n %{name}+nsatomicstore
Summary:        Bindings to the CoreData framework - feature "NSAtomicStore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsatomicstore) = %{version}

%description -n %{name}+nsatomicstore
This metapackage enables feature "NSAtomicStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsatomicstorecachenode
Summary:        Bindings to the CoreData framework - feature "NSAtomicStoreCacheNode" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsatomicstorecachenode) = %{version}
Provides:       crate(%{pkgname}/nsincrementalstorenode) = %{version}

%description -n %{name}+nsatomicstorecachenode
This metapackage enables feature "NSAtomicStoreCacheNode" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSIncrementalStoreNode" feature.

%package     -n %{name}+nsattributedescription
Summary:        Bindings to the CoreData framework - feature "NSAttributeDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsattributedescription) = %{version}

%description -n %{name}+nsattributedescription
This metapackage enables feature "NSAttributeDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbatchdeleterequest
Summary:        Bindings to the CoreData framework - feature "NSBatchDeleteRequest" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsbatchdeleterequest) = %{version}
Provides:       crate(%{pkgname}/nscompositeattributedescription) = %{version}
Provides:       crate(%{pkgname}/nspersistentstorerequest) = %{version}

%description -n %{name}+nsbatchdeleterequest
This metapackage enables feature "NSBatchDeleteRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSCompositeAttributeDescription", and "NSPersistentStoreRequest" features.

%package     -n %{name}+nsbatchinsertrequest
Summary:        Bindings to the CoreData framework - feature "NSBatchInsertRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbatchinsertrequest) = %{version}

%description -n %{name}+nsbatchinsertrequest
This metapackage enables feature "NSBatchInsertRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsbatchupdaterequest
Summary:        Bindings to the CoreData framework - feature "NSBatchUpdateRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsbatchupdaterequest) = %{version}

%description -n %{name}+nsbatchupdaterequest
This metapackage enables feature "NSBatchUpdateRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscoredatacorespotlightdelegate
Summary:        Bindings to the CoreData framework - feature "NSCoreDataCoreSpotlightDelegate"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nscoredatacorespotlightdelegate) = %{version}

%description -n %{name}+nscoredatacorespotlightdelegate
This metapackage enables feature "NSCoreDataCoreSpotlightDelegate" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nscustommigrationstage
Summary:        Bindings to the CoreData framework - feature "NSCustomMigrationStage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Provides:       crate(%{pkgname}/nscustommigrationstage) = %{version}

%description -n %{name}+nscustommigrationstage
This metapackage enables feature "NSCustomMigrationStage" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsderivedattributedescription
Summary:        Bindings to the CoreData framework - feature "NSDerivedAttributeDescription" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsderivedattributedescription) = %{version}
Provides:       crate(%{pkgname}/nsexpressiondescription) = %{version}

%description -n %{name}+nsderivedattributedescription
This metapackage enables feature "NSDerivedAttributeDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSExpressionDescription" feature.

%package     -n %{name}+nsentitydescription
Summary:        Bindings to the CoreData framework - feature "NSEntityDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsentitydescription) = %{version}

%description -n %{name}+nsentitydescription
This metapackage enables feature "NSEntityDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsentitymapping
Summary:        Bindings to the CoreData framework - feature "NSEntityMapping"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsentitymapping) = %{version}

%description -n %{name}+nsentitymapping
This metapackage enables feature "NSEntityMapping" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsentitymigrationpolicy
Summary:        Bindings to the CoreData framework - feature "NSEntityMigrationPolicy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsentitymigrationpolicy) = %{version}

%description -n %{name}+nsentitymigrationpolicy
This metapackage enables feature "NSEntityMigrationPolicy" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchindexdescription
Summary:        Bindings to the CoreData framework - feature "NSFetchIndexDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchindexdescription) = %{version}

%description -n %{name}+nsfetchindexdescription
This metapackage enables feature "NSFetchIndexDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchindexelementdescription
Summary:        Bindings to the CoreData framework - feature "NSFetchIndexElementDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchindexelementdescription) = %{version}

%description -n %{name}+nsfetchindexelementdescription
This metapackage enables feature "NSFetchIndexElementDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchrequest
Summary:        Bindings to the CoreData framework - feature "NSFetchRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nssortdescriptor) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchrequest) = %{version}

%description -n %{name}+nsfetchrequest
This metapackage enables feature "NSFetchRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchrequestexpression
Summary:        Bindings to the CoreData framework - feature "NSFetchRequestExpression"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nscoder) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchrequestexpression) = %{version}

%description -n %{name}+nsfetchrequestexpression
This metapackage enables feature "NSFetchRequestExpression" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsfetchedpropertydescription
Summary:        Bindings to the CoreData framework - feature "NSFetchedPropertyDescription" and 2 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchedpropertydescription) = %{version}
Provides:       crate(%{pkgname}/nspersistenthistorytoken) = %{version}
Provides:       crate(%{pkgname}/nsquerygenerationtoken) = %{version}

%description -n %{name}+nsfetchedpropertydescription
This metapackage enables feature "NSFetchedPropertyDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPersistentHistoryToken", and "NSQueryGenerationToken" features.

%package     -n %{name}+nsfetchedresultscontroller
Summary:        Bindings to the CoreData framework - feature "NSFetchedResultsController"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsindexpath) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsorderedcollectiondifference) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsfetchedresultscontroller) = %{version}

%description -n %{name}+nsfetchedresultscontroller
This metapackage enables feature "NSFetchedResultsController" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsincrementalstore
Summary:        Bindings to the CoreData framework - feature "NSIncrementalStore" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsincrementalstore) = %{version}
Provides:       crate(%{pkgname}/nsmigrationmanager) = %{version}

%description -n %{name}+nsincrementalstore
This metapackage enables feature "NSIncrementalStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSMigrationManager" feature.

%package     -n %{name}+nslightweightmigrationstage
Summary:        Bindings to the CoreData framework - feature "NSLightweightMigrationStage"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nslightweightmigrationstage) = %{version}

%description -n %{name}+nslightweightmigrationstage
This metapackage enables feature "NSLightweightMigrationStage" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobject
Summary:        Bindings to the CoreData framework - feature "NSManagedObject"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nskeyvalueobserving) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsmanagedobject) = %{version}

%description -n %{name}+nsmanagedobject
This metapackage enables feature "NSManagedObject" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectcontext
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectContext"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslock) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsundomanager) >= 0.2.2
Provides:       crate(%{pkgname}/nsmanagedobjectcontext) = %{version}

%description -n %{name}+nsmanagedobjectcontext
This metapackage enables feature "NSManagedObjectContext" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectid
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectID"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsmanagedobjectid) = %{version}

%description -n %{name}+nsmanagedobjectid
This metapackage enables feature "NSManagedObjectID" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectmodel
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectModel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsenumerator) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsmanagedobjectmodel) = %{version}

%description -n %{name}+nsmanagedobjectmodel
This metapackage enables feature "NSManagedObjectModel" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmanagedobjectmodelreference
Summary:        Bindings to the CoreData framework - feature "NSManagedObjectModelReference"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsmanagedobjectmodelreference) = %{version}

%description -n %{name}+nsmanagedobjectmodelreference
This metapackage enables feature "NSManagedObjectModelReference" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmappingmodel
Summary:        Bindings to the CoreData framework - feature "NSMappingModel"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsbundle) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nsmappingmodel) = %{version}

%description -n %{name}+nsmappingmodel
This metapackage enables feature "NSMappingModel" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsmergepolicy
Summary:        Bindings to the CoreData framework - feature "NSMergePolicy"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nsmergepolicy) = %{version}

%description -n %{name}+nsmergepolicy
This metapackage enables feature "NSMergePolicy" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainer
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainer) = %{version}

%description -n %{name}+nspersistentcloudkitcontainer
This metapackage enables feature "NSPersistentCloudKitContainer" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainerevent
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainerEvent"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsuuid) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainerevent) = %{version}

%description -n %{name}+nspersistentcloudkitcontainerevent
This metapackage enables feature "NSPersistentCloudKitContainerEvent" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentcloudkitcontainereventrequest
Summary:        Bindings to the CoreData framework - feature "NSPersistentCloudKitContainerEventRequest" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentcloudkitcontainereventrequest) = %{version}
Provides:       crate(%{pkgname}/nspersistenthistorychangerequest) = %{version}

%description -n %{name}+nspersistentcloudkitcontainereventrequest
This metapackage enables feature "NSPersistentCloudKitContainerEventRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "NSPersistentHistoryChangeRequest" feature.

%package     -n %{name}+nspersistentcontainer
Summary:        Bindings to the CoreData framework - feature "NSPersistentContainer"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentcontainer) = %{version}

%description -n %{name}+nspersistentcontainer
This metapackage enables feature "NSPersistentContainer" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistenthistorychange
Summary:        Bindings to the CoreData framework - feature "NSPersistentHistoryChange"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistenthistorychange) = %{version}

%description -n %{name}+nspersistenthistorychange
This metapackage enables feature "NSPersistentHistoryChange" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistenthistorytransaction
Summary:        Bindings to the CoreData framework - feature "NSPersistentHistoryTransaction"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsnotification) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistenthistorytransaction) = %{version}

%description -n %{name}+nspersistenthistorytransaction
This metapackage enables feature "NSPersistentHistoryTransaction" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstore
Summary:        Bindings to the CoreData framework - feature "NSPersistentStore"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentstore) = %{version}

%description -n %{name}+nspersistentstore
This metapackage enables feature "NSPersistentStore" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstorecoordinator
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreCoordinator"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nslock) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsvalue) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentstorecoordinator) = %{version}

%description -n %{name}+nspersistentstorecoordinator
This metapackage enables feature "NSPersistentStoreCoordinator" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstoredescription
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsurl) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentstoredescription) = %{version}

%description -n %{name}+nspersistentstoredescription
This metapackage enables feature "NSPersistentStoreDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspersistentstoreresult
Summary:        Bindings to the CoreData framework - feature "NSPersistentStoreResult"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nserror) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsprogress) >= 0.2.2
Provides:       crate(%{pkgname}/nspersistentstoreresult) = %{version}

%description -n %{name}+nspersistentstoreresult
This metapackage enables feature "NSPersistentStoreResult" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspropertydescription
Summary:        Bindings to the CoreData framework - feature "NSPropertyDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nspredicate) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspropertydescription) = %{version}

%description -n %{name}+nspropertydescription
This metapackage enables feature "NSPropertyDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nspropertymapping
Summary:        Bindings to the CoreData framework - feature "NSPropertyMapping"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdictionary) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsexpression) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsstring) >= 0.2.2
Provides:       crate(%{pkgname}/nspropertymapping) = %{version}

%description -n %{name}+nspropertymapping
This metapackage enables feature "NSPropertyMapping" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsrelationshipdescription
Summary:        Bindings to the CoreData framework - feature "NSRelationshipDescription"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsdata) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Provides:       crate(%{pkgname}/nsrelationshipdescription) = %{version}

%description -n %{name}+nsrelationshipdescription
This metapackage enables feature "NSRelationshipDescription" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nssavechangesrequest
Summary:        Bindings to the CoreData framework - feature "NSSaveChangesRequest"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsobject) >= 0.2.2
Requires:       crate(objc2-foundation-0.2/nsset) >= 0.2.2
Provides:       crate(%{pkgname}/nssavechangesrequest) = %{version}

%description -n %{name}+nssavechangesrequest
This metapackage enables feature "NSSaveChangesRequest" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+nsstagedmigrationmanager
Summary:        Bindings to the CoreData framework - feature "NSStagedMigrationManager"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(objc2-foundation-0.2/nsarray) >= 0.2.2
Provides:       crate(%{pkgname}/nsstagedmigrationmanager) = %{version}

%description -n %{name}+nsstagedmigrationmanager
This metapackage enables feature "NSStagedMigrationManager" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+all
Summary:        Bindings to the CoreData framework - feature "all"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/bitflags) = %{version}
Requires:       crate(%{pkgname}/block2) = %{version}
Requires:       crate(%{pkgname}/coredatadefines) = %{version}
Requires:       crate(%{pkgname}/coredataerrors) = %{version}
Requires:       crate(%{pkgname}/nsatomicstore) = %{version}
Requires:       crate(%{pkgname}/nsatomicstorecachenode) = %{version}
Requires:       crate(%{pkgname}/nsattributedescription) = %{version}
Requires:       crate(%{pkgname}/nsbatchdeleterequest) = %{version}
Requires:       crate(%{pkgname}/nsbatchinsertrequest) = %{version}
Requires:       crate(%{pkgname}/nsbatchupdaterequest) = %{version}
Requires:       crate(%{pkgname}/nscompositeattributedescription) = %{version}
Requires:       crate(%{pkgname}/nscoredatacorespotlightdelegate) = %{version}
Requires:       crate(%{pkgname}/nscustommigrationstage) = %{version}
Requires:       crate(%{pkgname}/nsderivedattributedescription) = %{version}
Requires:       crate(%{pkgname}/nsentitydescription) = %{version}
Requires:       crate(%{pkgname}/nsentitymapping) = %{version}
Requires:       crate(%{pkgname}/nsentitymigrationpolicy) = %{version}
Requires:       crate(%{pkgname}/nsexpressiondescription) = %{version}
Requires:       crate(%{pkgname}/nsfetchedpropertydescription) = %{version}
Requires:       crate(%{pkgname}/nsfetchedresultscontroller) = %{version}
Requires:       crate(%{pkgname}/nsfetchindexdescription) = %{version}
Requires:       crate(%{pkgname}/nsfetchindexelementdescription) = %{version}
Requires:       crate(%{pkgname}/nsfetchrequest) = %{version}
Requires:       crate(%{pkgname}/nsfetchrequestexpression) = %{version}
Requires:       crate(%{pkgname}/nsincrementalstore) = %{version}
Requires:       crate(%{pkgname}/nsincrementalstorenode) = %{version}
Requires:       crate(%{pkgname}/nslightweightmigrationstage) = %{version}
Requires:       crate(%{pkgname}/nsmanagedobject) = %{version}
Requires:       crate(%{pkgname}/nsmanagedobjectcontext) = %{version}
Requires:       crate(%{pkgname}/nsmanagedobjectid) = %{version}
Requires:       crate(%{pkgname}/nsmanagedobjectmodel) = %{version}
Requires:       crate(%{pkgname}/nsmanagedobjectmodelreference) = %{version}
Requires:       crate(%{pkgname}/nsmappingmodel) = %{version}
Requires:       crate(%{pkgname}/nsmergepolicy) = %{version}
Requires:       crate(%{pkgname}/nsmigrationmanager) = %{version}
Requires:       crate(%{pkgname}/nsmigrationstage) = %{version}
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainer) = %{version}
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainerevent) = %{version}
Requires:       crate(%{pkgname}/nspersistentcloudkitcontainereventrequest) = %{version}
Requires:       crate(%{pkgname}/nspersistentcloudkitcontaineroptions) = %{version}
Requires:       crate(%{pkgname}/nspersistentcontainer) = %{version}
Requires:       crate(%{pkgname}/nspersistenthistorychange) = %{version}
Requires:       crate(%{pkgname}/nspersistenthistorychangerequest) = %{version}
Requires:       crate(%{pkgname}/nspersistenthistorytoken) = %{version}
Requires:       crate(%{pkgname}/nspersistenthistorytransaction) = %{version}
Requires:       crate(%{pkgname}/nspersistentstore) = %{version}
Requires:       crate(%{pkgname}/nspersistentstorecoordinator) = %{version}
Requires:       crate(%{pkgname}/nspersistentstoredescription) = %{version}
Requires:       crate(%{pkgname}/nspersistentstorerequest) = %{version}
Requires:       crate(%{pkgname}/nspersistentstoreresult) = %{version}
Requires:       crate(%{pkgname}/nspropertydescription) = %{version}
Requires:       crate(%{pkgname}/nspropertymapping) = %{version}
Requires:       crate(%{pkgname}/nsquerygenerationtoken) = %{version}
Requires:       crate(%{pkgname}/nsrelationshipdescription) = %{version}
Requires:       crate(%{pkgname}/nssavechangesrequest) = %{version}
Requires:       crate(%{pkgname}/nsstagedmigrationmanager) = %{version}
Provides:       crate(%{pkgname}/all) = %{version}

%description -n %{name}+all
This metapackage enables feature "all" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+alloc
Summary:        Bindings to the CoreData framework - feature "alloc"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5/alloc) >= 0.5.1
Requires:       crate(objc2-0.5/alloc) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/alloc) >= 0.2.2
Provides:       crate(%{pkgname}/alloc) = %{version}

%description -n %{name}+alloc
This metapackage enables feature "alloc" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+bitflags
Summary:        Bindings to the CoreData framework - feature "bitflags"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(bitflags-2) >= 2.5.0
Requires:       crate(objc2-foundation-0.2/bitflags) >= 0.2.2
Provides:       crate(%{pkgname}/bitflags) = %{version}

%description -n %{name}+bitflags
This metapackage enables feature "bitflags" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+block2
Summary:        Bindings to the CoreData framework - feature "block2"
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(block2-0.5) >= 0.5.1
Requires:       crate(objc2-foundation-0.2/block2) >= 0.2.2
Provides:       crate(%{pkgname}/block2) = %{version}

%description -n %{name}+block2
This metapackage enables feature "block2" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

%package     -n %{name}+std
Summary:        Bindings to the CoreData framework - feature "std" and 1 more
Requires:       crate(%{pkgname}) = %{version}
Requires:       crate(%{pkgname}/alloc) = %{version}
Requires:       crate(bitflags-2/std) >= 2.5.0
Requires:       crate(block2-0.5/std) >= 0.5.1
Requires:       crate(objc2-0.5/std) >= 0.5.2
Requires:       crate(objc2-foundation-0.2/std) >= 0.2.2
Provides:       crate(%{pkgname}/default) = %{version}
Provides:       crate(%{pkgname}/std) = %{version}

%description -n %{name}+std
This metapackage enables feature "std" for the Rust objc2-core-data crate, by pulling in any additional dependencies needed by that feature.

Additionally, this package also provides the "default" feature.

%files
%{_datadir}/cargo/registry/%{crate_name}-%{version}/

%changelog
%autochangelog

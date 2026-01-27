# Cloud Firestore

## Cloud Firestore

Installation and getting started with Firestore.

### Installation

This module requires that the@react-native-firebase/appmodule is already setup and installed. To install the "app" module, view theGetting Starteddocumentation.

```
# Install & setup the app module
yarn add @react-native-firebase/app

# Install the firestore module
yarn add @react-native-firebase/firestore

# If you're developing your app using iOS, run this command
cd ios/ && pod install

```

If you're using an older version of React Native without autolinking support, or wish to integrate into an existing project,
you can follow the manual installation steps foriOSandAndroid.

If you have started to receive aapp:mergeDexDebugerror after adding Cloud Firestore, please read theEnabling Multidexdocumentation for more information on how to resolve this error.

### What does it do

Firestore is a flexible, scalable NoSQL cloud database to store and sync data. It keeps your data in sync across client
apps through realtime listeners and offers offline support so you can build responsive apps that work regardless of network
latency or Internet connectivity.

### Usage

#### Collections & Documents

Cloud Firestore stores data within "documents", which are contained within "collections", and documents can also contain
collections. For example, we could store a list of our users documents within a "Users" collection. Thecollectionmethod
allows us to reference a collection within our code:

```
import firestore from '@react-native-firebase/firestore';

const usersCollection = firestore().collection('Users');

```

Thecollectionmethod returns aCollectionReferenceclass, which provides
properties and methods to query and fetch the data from Cloud Firestore. We can also directly reference a single document
on the collection by calling thedocmethod:

```
import firestore from '@react-native-firebase/firestore';

// Get user document with an ID of ABC
const userDocument = firestore().collection('Users').doc('ABC');

```

Thedocmethod returns aDocumentReference.

A document can contain different types of data, including scalar values (strings, booleans, numbers), arrays (lists) and
objects (maps) along with specific Cloud Firestore data such asTimestamps,GeoPoints,Blobsand more.

#### Read Data

Cloud Firestore provides the ability to read the value of a collection or document. This can be read one-time, or provide
realtime updates when the data within a query changes.

##### One-time read

To read a collection or document once, call thegetmethod on aCollectionReferenceorDocumentReference:

```
import firestore from '@react-native-firebase/firestore';

const users = await firestore().collection('Users').get();
const user = await firestore().collection('Users').doc('ABC').get();

```

##### Realtime changes

To setup an active listener to react to any changes to the query, call theonSnapshotmethod with an event handler callback.
For example, to watch the entire "Users" collection for when any documents are changed (removed, added, modified):

```
import firestore from '@react-native-firebase/firestore';

function onResult(QuerySnapshot) {
 console.log('Got Users collection result.');
}

function onError(error) {
 console.error(error);
}

firestore().collection('Users').onSnapshot(onResult, onError);

```

TheonSnapshotmethod also returns a function, allowing you to unsubscribe from events. This can be used within anyuseEffecthooks to automatically unsubscribe when the hook needs to unsubscribe itself:

```
import React, { useEffect } from 'react';
import firestore from '@react-native-firebase/firestore';

function User({ userId }) {
 useEffect(() => {
 const subscriber = firestore()
 .collection('Users')
 .doc(userId)
 .onSnapshot(documentSnapshot => {
 console.log('User data: ', documentSnapshot.data());
 });

 // Stop listening for updates when no longer required
 return () => subscriber();
 }, [userId]);
}

```

Realtime changes via theonSnapshotmethod can be applied to both collections and documents.

##### Snapshots

Once a query has returned a result, Firestore returns either aQuerySnapshot(for
collection queries) or aDocumentSnapshot(for document queries). These snapshots
provide the ability to view the data, view query metadata (such as whether the data was from local cache), whether the
document exists or not and more.

AQuerySnapshotreturned from a collection query allows you to inspect the collection,
such as how many documents exist within it, access to the documents within the collection, any changes since the last query
and more.

To access the documents within aQuerySnapshot, call theforEachmethod:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .get()
 .then(querySnapshot => {
 console.log('Total users: ', querySnapshot.size);

 querySnapshot.forEach(documentSnapshot => {
 console.log('User ID: ', documentSnapshot.id, documentSnapshot.data());
 });
 });

```

Each child document of aQuerySnapshotis aQueryDocumentSnapshot, which
allows you to access specific information about a document (see below).

ADocumentSnapshotis returned from a query to a specific document, or as part
of the documents returned via aQuerySnapshot. The snapshot provides the ability
to view a documents data, metadata and whether a document actually exists.

To view a documents data, call thedatamethod on the snapshot:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .doc('ABC')
 .get()
 .then(documentSnapshot => {
 console.log('User exists: ', documentSnapshot.exists);

 if (documentSnapshot.exists) {
 console.log('User data: ', documentSnapshot.data());
 }
 });

```

A snapshot also provides a helper function to easily access deeply nested data within a document. Call thegetmethod
with a dot-notated path:

```
function getUserZipCode(documentSnapshot) {
 return documentSnapshot.get('info.address.zipcode');
}

firestore()
 .collection('Users')
 .doc('ABC')
 .get()
 .then(documentSnapshot => getUserZipCode(documentSnapshot))
 .then(zipCode => {
 console.log('Users zip code is: ', zipCode);
 });

```

##### Querying

Cloud Firestore offers advanced capabilities for querying collections.

To filter documents within a collection, thewheremethod can be chained onto a collection reference. Filtering supports
equality checks and "in" queries. For example, to filter users where their age is greater or equal than 18 years old:

```
firestore()
 .collection('Users')
 // Filter results
 .where('age', '>=', 18)
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

Cloud Firestore also supports array membership queries. For example, to filter users who speak both English (en) or
French (fr), use theinfilter:

```
firestore()
 .collection('Users')
 // Filter results
 .where('languages', 'in', ['en', 'fr'])
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

To learn more about all of the querying capabilities Cloud Firestore has to offer, view theFirebase documentation.

It is now possible to use theFilterinstance to make queries. They can be used with the existing query API.
For example, you could chain like so:

```
const snapshot = await firestore()
 .collection('Users')
 .where(Filter('user', '==', 'Tim'))
 .where('email', '==', 'tim@example.com')
 .get();

```

You can use theFilter.and()static method to make logical AND queries:

```
const snapshot = await firestore()
 .collection('Users')
 .where(Filter.and(Filter('user', '==', 'Tim'), Filter('email', '==', 'tim@example.com')))
 .get();

```

You can use theFilter.or()static method to make logical OR queries:

```
const snapshot = await firestore()
 .collection('Users')
 .where(
 Filter.or(
 Filter.and(Filter('user', '==', 'Tim'), Filter('email', '==', 'tim@example.com')),
 Filter.and(Filter('user', '==', 'Dave'), Filter('email', '==', 'dave@example.com')),
 ),
 )
 .get();

```

For an understanding of what queries are possible, please consult the query limitation documentation on the officialFirebase Firestore documentation.

To limit the number of documents returned from a query, use thelimitmethod on a collection reference:

```
firestore()
 .collection('Users')
 // Filter results
 .where('age', '>=', 18)
 // Limit results
 .limit(20)
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

The above example both filters the users by age and limits the documents returned to 20.

To order the documents by a specific value, use theorderBymethod:

```
firestore()
 .collection('Users')
 // Order results
 .orderBy('age', 'desc')
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

The above example orders all user in the snapshot by age in descending order.

To start and/or end the query at a specific point within the collection, you can pass either a value to thestartAt,endAt,startAfterorendBeforemethods. You must specify an order to use pointers, for example:

```
firestore()
 .collection('Users')
 .orderBy('age', 'desc')
 .startAt(18)
 .endAt(30)
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

The above query orders the users by age in descending order, but only returns users whose age is between 18 and 30.

You can further specify aDocumentSnapshotinstead of a specific value. For example:

```
const userDocumentSnapshot = await firestore().collection('Users').doc('DEF').get();

firestore()
 .collection('Users')
 .orderBy('age', 'desc')
 .startAt(userDocumentSnapshot)
 .get()
 .then(querySnapshot => {
 /* ... */
 });

```

The above query orders the users by age in descending order, however only returns documents whose order starts at the user
with an ID ofDEF.

Cloud Firestore does not support the following types of queries:

- Queries with range filters on different fields, as described in the previous section.

#### Writing Data

TheFirebase documentationprovides great examples
on best practices on how to structure your data. We highly recommend reading the guide before building out your database.

For a more in-depth look at what is possible when writing data to Firestore please refer to thisdocumentation

#### Adding documents

To add a new document to a collection, use theaddmethod on aCollectionReference:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .add({
 name: 'Ada Lovelace',
 age: 30,
 })
 .then(() => {
 console.log('User added!');
 });

```

Theaddmethod adds the new document to your collection with a random unique ID. If you'd like to specify your own ID,
call thesetmethod on aDocumentReferenceinstead:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .doc('ABC')
 .set({
 name: 'Ada Lovelace',
 age: 30,
 })
 .then(() => {
 console.log('User added!');
 });

```

##### Updating documents

Thesetmethod exampled above replaces any existing data on a givenDocumentReference.
if you'd like to update a document instead, use theupdatemethod:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .doc('ABC')
 .update({
 age: 31,
 })
 .then(() => {
 console.log('User updated!');
 });

```

The method also provides support for updating deeply nested values via dot-notation:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .doc('ABC')
 .update({
 'info.address.zipcode': 94040,
 })
 .then(() => {
 console.log('User updated!');
 });

```

Cloud Firestore supports storing and manipulating values on your database, such asTimestamps,GeoPoints,Blobsand array management.

To storeGeoPointvalues, provide the latitude and longitude to a new instance of the
class:

```
firestore()
 .doc('users/ABC')
 .update({
 'info.address.location': new firestore.GeoPoint(53.483959, -2.244644),
 });

```

To store aBlob(for example of aBase64image string), provide the string to the staticfromBase64Stringmethod on the class:

```
firestore()
 .doc('users/ABC')
 .update({
 'info.avatar': firestore.Blob.fromBase64String('data:image/png;base64,iVBOR...'),
 });

```

When storing timestamps, it is recommended you use theserverTimestampstatic method on theFieldValueclass. When written to the database, the Firebase servers will write a new timestamp based on their time, rather than the clients. This helps
resolve any data consistency issues with different client timezones:

```
firestore().doc('users/ABC').update({
 createdAt: firestore.FieldValue.serverTimestamp(),
});

```

Cloud Firestore also allows for storing arrays. To help manage the values with an array (adding or removing) the API
exposes anarrayUnionandarrayRemovemethods on theFieldValueclass.

To add a new value to an array (if value does not exist, will not add duplicate values):

```
firestore()
 .doc('users/ABC')
 .update({
 fcmTokens: firestore.FieldValue.arrayUnion('ABCDE123456'),
 });

```

To remove a value from the array (if the value exists):

```
firestore()
 .doc('users/ABC')
 .update({
 fcmTokens: firestore.FieldValue.arrayRemove('ABCDE123456'),
 });

```

#### Removing data

You can delete documents within Cloud Firestore using thedeletemethod on aDocumentReference:

```
import firestore from '@react-native-firebase/firestore';

firestore()
 .collection('Users')
 .doc('ABC')
 .delete()
 .then(() => {
 console.log('User deleted!');
 });

```

At this time, you cannot delete an entire collection without use of a Firebase Admin SDK.

If a document contains any sub-collections, these will not be deleted from database. You must delete
any sub-collections yourself.

If you need to remove a specific property with a document, rather than the document itself, you can use thedeletemethod on theFieldValueclass:

```
firestore().collection('Users').doc('ABC').update({
 fcmTokens: firestore.FieldValue.delete(),
});

```

#### Transactions

Transactions are a way to always ensure a write occurs with the latest information available on the server. Transactions
never partially apply writes & all writes execute at the end of a successful transaction.

Transactions are useful when you want to update a field's value based on its current value, or the value of some other field.
If you simply want to write multiple documents without using the document's current state, abatch writewould be more appropriate.

When using transactions, note that:

- Read operations must come before write operations.
- A function calling a transaction (transaction function) might run more than once if a concurrent edit affects a document that the transaction reads.
- Transaction functions should not directly modify application state (return a value from theupdateFunction).
- Transactions will fail when the client is offline.
Imagine a scenario whereby an app has the ability to "Like" user posts. Whenever a user presses the "Like" button,
a "likes" value (number of likes) on a "Posts" collection document increments. Without transactions, we'd first need to read
the existing value and then increment that value in two separate operations.

On a high traffic application, the value on the server could already have changed by the time the operation sets a new value,
causing the actual number to not be consistent.

Transactions remove this issue by atomically updating the value on the server. If the value changes whilst the transaction
is executing, it will retry. This always ensures the value on the server is used rather than the client value.

To execute a new transaction, call therunTransactionmethod:

```
import firestore from '@react-native-firebase/firestore';

function onPostLike(postId) {
 // Create a reference to the post
 const postReference = firestore().doc(`posts/${postId}`);

 return firestore().runTransaction(async transaction => {
 // Get post data first
 const postSnapshot = await transaction.get(postReference);

 if (!postSnapshot.exists) {
 throw 'Post does not exist!';
 }

 transaction.update(postReference, {
 likes: postSnapshot.data().likes + 1,
 });
 });
}

onPostLike('ABC')
 .then(() => console.log('Post likes incremented via a transaction'))
 .catch(error => console.error(error));

```

#### Batch write

If you do not need to read any documents in your operation set, you can execute multiple write operations as a single batch
that contains any combination ofset,update, ordeleteoperations. A batch of writes completes atomically and can
write to multiple documents.

First, create a new batch instance via thebatchmethod, perform operations on the batch and finally commit it once ready.
The example below shows how to delete all documents in a collection in a single operation:

```
import firestore from '@react-native-firebase/firestore';

async function massDeleteUsers() {
 // Get all users
 const usersQuerySnapshot = await firestore().collection('Users').get();

 // Create a new batch instance
 const batch = firestore().batch();

 usersQuerySnapshot.forEach(documentSnapshot => {
 batch.delete(documentSnapshot.ref);
 });

 return batch.commit();
}

massDeleteUsers().then(() => console.log('All users deleted in a single batch operation.'));

```

#### Secure your data

It is important that you understand how to write rules in your Firebase console to ensure that your data is secure. Please
follow the Firebase Firestore documentation onsecurity.

#### Offline Capabilities

Firestore provides out of the box support for offline capabilities. When reading and writing data, Firestore uses a local
database which synchronizes automatically with the server. Firestore functionality continues when users are offline, and
automatically handles data migration to the server when they regain connectivity.

This functionality is enabled by default, however it can be disabled if you need it to be disabled (e.g. on apps containing
sensitive information). Thesettings()method must be called before any Firestore interaction is performed, otherwise it will only take effect on the next app launch:

```
import firestore from '@react-native-firebase/firestore';

async function bootstrap() {
 await firestore().settings({
 persistence: false, // disable offline persistence
 });
}

```

#### Data bundles

Cloud Firestore data bundles are static data files built by you from Cloud Firestore document and query snapshots,
and published by you on a CDN, hosting service or other solution. Once a bundle is loaded, a client app can query documents
from the local cache or the backend.

To load and query data bundles, use theloadBundleandnamedQuerymethods:

```
import firestore from '@react-native-firebase/firestore';

// load the bundle contents
const response = await fetch('https://api.example.com/bundles/latest-stories');
const bundle = await response.text();
await firestore().loadBundle(bundle);

// query the results from the cache
// note: omitting "source: cache" will query the Firestore backend
const query = firestore().namedQuery('latest-stories-query');
const snapshot = await query.get({ source: 'cache' });

```

You can build data bundles with the Admin SDK. For more information about building and serving data bundles, see Firebase Firestore main documentation onData bundlesas well as their "Bundle Solutions" page